from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.network import Armor
from diagrams.gcp.compute import Run, Functions
from diagrams.gcp.database import SQL, Datastore
from diagrams.generic.device import Mobile, Tablet
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.monitoring import Grafana
from diagrams.programming.framework import Flutter, React, Spring
from diagrams.saas.cdn import Cloudflare
from diagrams.k8s.compute import Pod


def drawArchitecture(is_service=False):
    with Cluster("Client"):
        client = Cloudflare("Client") if not is_service else React("Client")

    with Cluster("Google Cloud"):
        armor = Armor("Armor")

        with Cluster("Back-end API"):
            backend_run = Run("Main Back-end API") if not is_service else Spring("Main Back-end API")
            backend_sql = SQL("Backend DB") if not is_service else PostgreSQL("Backend DB")
            backend_nosql = Datastore("Backend Palette DB")

        with Cluster("Algorithm Cluster"):
            algorithm1 = Pod("Algorithm 1") if not is_service else Run("Algorithm 1")
            algorithm2 = Pod("Algorithm 2") if not is_service else Run("Algorithm 1")
            algorithm3 = Pod("Algorithm 3") if not is_service else Run("Algorithm 1")
    
    client >> armor

    armor >> backend_run

    backend_run >> backend_sql
    backend_run >> backend_nosql
    backend_sql >> backend_run
    backend_nosql >> backend_run
    
    

with Diagram("GCP Architecture", filename="docs/architecture/imgs/gcp_architecture", show=False, direction="TB"):
    drawArchitecture()

with Diagram("Service Architecture", filename="docs/architecture/imgs/service_architecture", show=False, direction="TB"):
    drawArchitecture(is_service=True)
