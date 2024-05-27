from diagrams import Diagram, Cluster
from diagrams.gcp.network import Armor
from diagrams.gcp.compute import Run, Functions
from diagrams.gcp.database import SQL, Datastore
from diagrams.onprem.database import PostgreSQL
from diagrams.programming.framework import React, Spring
from diagrams.saas.cdn import Cloudflare
from diagrams.generic.compute import Rack
from diagrams.gcp.storage import Storage


def drawArchitecture(is_service=False):
    with Cluster("Client"):
        client = Cloudflare("Client") if not is_service else React("Client")

    with Cluster("Google Cloud"):
        armor = Armor("Armor")

        with Cluster("Back-end API"):
            backend_run = Run("Main/Algorithm Back-end API") if not is_service else Spring("Main Back-end API")
            backend_sql = SQL("Backend DB") if not is_service else PostgreSQL("Backend DB")
            backend_storage = Storage("Backend Storage")

            if is_service:
                algorithm_server = Spring("Algorithm Back-end Server")

        with Cluster("Algorithm Cluster"):
            algorithm1 = Functions("Algorithm 1")
            algorithm2 = Functions("Algorithm 2")
            algorithm3 = Functions("Algorithm 3")
            algorithm_cluster = [algorithm1, algorithm2, algorithm3]

    with Cluster("External API"):
        map_api = Rack("Google map API")
        satellite_api = Rack("Satellite image API")

    client >> armor
    client >> map_api

    armor >> backend_run

    backend_run >> backend_sql
    backend_sql >> backend_run

    if is_service:
        algorithm_server >> backend_sql
        backend_sql >> algorithm_server

        backend_storage >> algorithm_server
        algorithm_server >> backend_storage

        algorithm_server >> satellite_api
    else:
        backend_run >> satellite_api

        backend_storage >> backend_run
        backend_run >> backend_storage

    for algo in algorithm_cluster:
        if is_service:
            algorithm_server >> algo
            algo >> algorithm_server
        else:
            backend_run >> algo
            algo >> backend_run


with Diagram("GCP Architecture", filename="docs/architecture/imgs/gcp_architecture", show=False, direction="TB"):
    drawArchitecture()

with Diagram(
    "Service Architecture", filename="docs/architecture/imgs/service_architecture", show=False, direction="TB"
):
    drawArchitecture(is_service=True)
