# Data Analysis and Extraction

## Main Features and Responsibilities

- Input Information
  - algorithm backend API -> algorithm cluster
- Analyze and Extract Data
  - Handled by the algorithm cluster
- Return Data
  - algorithm cluster -> algorithm backend API

## Overview

For details on each algorithm, refer to [Each Algorithm](./algorithm/README.md).
For the sequence diagram, refer to [Sequence Diagram](./system/sequence/algorithm.md).

This function, which is a data processing phase, operates solely on the communication between the Backend Server and the Algorithm Cluster.
The Algorithm Cluster cannot access anything outside the GCP (Google Cloud Platform). Each Algorithm Function belonging to the Algorithm Cluster registers the information it needs with the Backend Server in advance. The Backend Server notifies each Algorithm Function when the information (and the external APIs associated with that information) is updated. This allows each Algorithm Function to process data with the latest information and return the results to the Backend Server.

For this reason, the Algorithm Function is event-driven.
