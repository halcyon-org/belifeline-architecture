import architecture

from diagrams import Diagram

with Diagram("Infra Server", filename="docs/architecture/imgs/infra_server", show=False, direction="TB"):
    architecture.drawInfraServer()

with Diagram("Infra Service", filename="docs/architecture/imgs/infra_service", show=False, direction="TB"):
    architecture.drawInfraService()

with Diagram(
    "Service Architecture", filename="docs/architecture/imgs/service_architecture", show=False, direction="TB"
):
    architecture.drawServiceArchitecture()
