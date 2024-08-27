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
from diagrams.programming.language import Go, Python
from diagrams.onprem.database import PostgreSQL
from diagrams.generic.storage import Storage
from diagrams.k8s.controlplane import API
from diagrams.k8s.compute import Cronjob
from diagrams.gcp.network import Armor
from diagrams.generic.device import Mobile
from diagrams.programming.flowchart import Database


def drawServiceArchitecture():
    with Cluster("Kizuna Cluster"):
        kizuna = Go("kizuna")
        db = PostgreSQL("postgresql")
        storage = Storage("S3 (MinIO  extends TrueNAS)")

        kizuna >> Edge(label="gorm") >> db
        kizuna >> Edge(label="minio-go") >> storage

        with Cluster("Cronjob Cluster"):
            cronjob = Cronjob("Cronjob")
            kizuna_ext = Go("Kizuna External Info batch")

            cronjob - kizuna_ext

        kizuna_ext >> Edge(label="HTTP API") >> kizuna

    with Cluster("Koyo Cluster"):
        k8s_api = API("Kubernetes API")
        koyo = [Python("koyo"), Python("koyo"), Python("koyo"), Python("koyo")]

        k8s_api - koyo

    with Cluster("Google Cloud"):
        sevpn = ComputeEngine("SoftEther VPN")
        armor = Armor()

    kizuna >> Edge(label="client-go") >> k8s_api

    Mobile() >> armor >> sevpn >> kizuna

    ext_api = Database("External API")
    kizuna >> ext_api
    kizuna_ext >> ext_api
