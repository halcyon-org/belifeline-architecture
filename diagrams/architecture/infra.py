from diagrams import Cluster, Diagram, Edge
from diagrams.gcp.compute import ComputeEngine
from diagrams.gcp.storage import Storage
from diagrams.generic.network import VPN
from diagrams.k8s.compute import Pod
from diagrams.k8s.controlplane import Kubelet
from diagrams.onprem.database import Influxdb
from diagrams.onprem.gitops import Argocd
from diagrams.onprem.iac import Ansible, Terraform
from diagrams.onprem.logging import Loki
from diagrams.onprem.monitoring import Grafana, Prometheus
from diagrams.onprem.proxmox import Pve
from diagrams.onprem.vcs import Github
from diagrams.saas.cdn import Cloudflare


def drawInfraServer():
    with Cluster("GitHub"):
        github = Github("GitHub")
        ansible = Ansible("Ansible")
        terraform = Terraform("Terraform")

        github >> ansible
        github >> terraform

    with Cluster("Cloudflare"):
        tunnel = Cloudflare("Tunnel")

    with Cluster("Google Cloud"):
        sevpn = ComputeEngine("SoftEther VPN")
        storage = Storage("Storage")

        cloud = [sevpn, storage]

    with Cluster("On-premises"):
        with Cluster("ProxmoxVE"):
            souzou08 = Pve("souzou08")
            souzou03 = Pve("souzou03")
            souzou04 = Pve("souzou04")
            souzou05 = Pve("souzou05")

            pve = [souzou08, souzou03, souzou04, souzou05]

            with Cluster("VM"):
                with Cluster("subaru"):
                    subaru01 = Kubelet("subaru01")
                    subaru02 = Pod("subaru02")
                    subaru03 = Pod("subaru03")

                    subaru = [subaru01, subaru02, subaru03]

                    souzou08 - subaru01
                    souzou03 - subaru02
                    souzou04 - subaru03

    sevpn >> tunnel
    pve >> Edge(color="blue") >> sevpn

    ansible >> pve
    ansible >> sevpn
    terraform >> cloud


def drawInfraService():
    with Cluster("Cloudflare"):
        tunnel = Cloudflare("Tunnel")
        metrics_tunnel = Cloudflare("Metrics Tunnel")

    with Cluster("shiron private cloud"):
        influxdb = Influxdb("InfluxDB")
        grafana = Grafana("Grafana")

    with Cluster("Google Cloud"):
        with Cluster("SEVPN Instance"):
            sevpn = VPN("SoftEther VPN")
            prometheus = Prometheus("Blackbox Exporter")
            loki = Loki("Loki")

    with Cluster("On-premises"):
        with Cluster("ProxmoxVE"):
            pve = Pve("Souzou cluster")

            with Cluster("VM"):
                with Cluster("subaru"):
                    subaru01 = Kubelet("subaru01")
                    subaru02 = Pod("subaru02")
                    subaru03 = Pod("subaru03")

                    subaru = [subaru01, subaru02, subaru03]

                    pve - subaru

                    with Cluster("Pod"):
                        argocd = Argocd("ArgoCD")
                        prometheus - argocd
                        loki - argocd
                        grafana - argocd

    sevpn >> tunnel
    pve >> Edge(color="blue") >> sevpn
    prometheus >> pve
    pve >> influxdb

    prometheus >> metrics_tunnel
    loki >> metrics_tunnel

    grafana - metrics_tunnel
    grafana - influxdb
