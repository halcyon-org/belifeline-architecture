# Algorithm Cluster Sequence Diagram

The Algorithm Cluster (Algorithm function) is event-driven. There are three types of events: initial startup (information registration), external information updates, and parameter-specific requests.

For each event:

- Initial Startup
  - Registers algorithm information upon the release of the Algorithm Function
  - Analyzes data based on the information available at that time
- External Information Update
  - Updates data when external information (such as external APIs) is updated
- Parameter-Specific Request
  - Generates data when data not currently stored is requested through the provider

## Initial Startup

For details on algorithm information, refer to [Data Definition #Algorithm Information](../data.md#アルゴリズム情報)

```mermaid
sequenceDiagram
    participant server as Algorithm Backend
    participant db as Database
    participant func as Algorithm Function
    server ->> func: Call initial startup event
    func ->> server: Register algorithm information (requested information, etc.)
    server ->> db: Save information
    server ->> func: Return external information based on algorithm information
    func ->> func: Data analysis and extraction
    func ->> server: Return data
    server ->> db: Save data
```

## External Information Update

```mermaid
sequenceDiagram
    participant server as Algorithm Backend
    participant db as Database
    participant func as Algorithm Function
    server ->> func: Call external information update event
    func ->> server: Request information
    server ->> func: Return external information based on the request
    func ->> func: Data analysis and extraction
    func ->> server: Return data
```

## Parameter-Specific Request

```mermaid
sequenceDiagram
    participant provider as Provider
    participant server as Algorithm Backend
    participant db as Database
    participant func as Algorithm Function
    provider ->> server: Data request
    server ->> func: Call initial startup event
    func ->> server: Register algorithm information (requested information, etc.)
    server ->> db: Save information
    server ->> func: Return data based on information
    server ->> provider: Data update notification
```
