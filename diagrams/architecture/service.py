from diagrams import Cluster, Diagram, Edge
from diagrams.gcp.compute import ComputeEngine
from diagrams.gcp.network import Armor
from diagrams.gcp.storage import Storage
from diagrams.generic.device import Mobile
from diagrams.generic.network import VPN
from diagrams.generic.storage import Storage
from diagrams.k8s.compute import Cronjob, Pod
from diagrams.k8s.controlplane import API, Kubelet
from diagrams.onprem.database import Influxdb, PostgreSQL
from diagrams.onprem.gitops import Argocd
from diagrams.onprem.iac import Ansible, Terraform
from diagrams.onprem.logging import Loki
from diagrams.onprem.monitoring import Grafana, Prometheus
from diagrams.onprem.proxmox import Pve
from diagrams.onprem.vcs import Github
from diagrams.programming.flowchart import Database
from diagrams.programming.language import Go, Python
from diagrams.saas.cdn import Cloudflare


def drawServiceArchitecture():
    with Cluster("Kizuna Cluster"):
        kizuna = Go("Kizuna")
        db = PostgreSQL("postgresql")
        storage = Storage("S3 (MinIO  extends TrueNAS)")

        kizuna >> Edge(label="gorm") >> db
        kizuna >> Edge(label="minio-go") >> storage

        with Cluster("Love Cluster"):
            cronjob = Cronjob("Cronjob")
            love = Go("Love")

            cronjob - love

        love >> Edge(label="HTTP API") >> kizuna

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
    love >> ext_api
