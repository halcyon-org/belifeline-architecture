# System Configuration

## Overview

- The cloud infrastructure uses GCP (Google Cloud Platform).
- The design is fundamentally serverless.

### Configuration Diagram Explanation

- Client
  - Client (Remix)
    - Creates a web application using Remix.
    - Overlays a heat map obtained from the Backend API onto a map provided by some Map API.
    - Hosted on Cloudflare Pages.
- GCP
  - Armor
    - Serves as a gateway connecting GCP to the outside world for DDoS and bot protection.
    - Inbound traffic passes through Armor, while outbound traffic does not to reduce data transfer costs.
  - Backend API
    - Consists of two systems: Main and Algorithm, with the Algorithm system being accessible only within GCP.
    - The Main system is accessible externally (provides APIs for the Client).
    - The Algorithm API controls the Algorithm Cluster.
    - While Main and Algorithm systems are essentially the same Backend, they are separated by different paths.
  - Backend DB
    - Temporarily using PostgreSQL.
    - Considering whether to use PostGIS for heat map storage or another DB (such as BigQuery).
  - Backend Storage
    - Temporarily stores satellite images and similar data.
- Algorithm Cluster

### System Configuration Diagrams

![Cloud Configuration Diagram](./imgs/gcp_architecture.png)

![Service Configuration Diagram](./imgs/service_architecture.png)