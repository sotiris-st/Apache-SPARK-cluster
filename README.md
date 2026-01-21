# Apache Spark Standalone Cluster (Client Mode)

## Overview

This repository demonstrates a **local Apache Spark standalone cluster** and its orchestration using **Apache Airflow** in **client mode**.  
The goal is to showcase Spark architecture, job execution, and observability **without relying on YARN, Mesos, or Kubernetes**, making it ideal for local development.

The project is structured in two stages:

1. **Spark Standalone Cluster** (Spark Master, Workers, History Server)
2. **Airflow Orchestration** using `SparkSubmitOperator` with Postgres and MinIO

This section describes **Stage 1: Spark Standalone Cluster**.

---

## Spark Standalone Architecture

The standalone Spark setup consists of:

- Spark Master
- Two Spark Workers
- Spark History Server
- External Docker volumes for Spark event logs and job files

All components run as **Docker containers** connected via a shared Docker network.

---

## Spark Job Execution (Client Mode)

Spark jobs are executed in **client mode** by submitting them directly to the Spark Master.

A shared directory is mounted at:

```
/tmp/spark-jobs
```

This directory is backed by a Docker volume so that Spark jobs persist across container restarts.

### Example Job

A sample PySpark job (`test.py`) performs:

- DataFrame creation
- Data cleaning
- Join operations
- Aggregation
- Action triggers (`show`, `count`)

This verifies:
- Executor allocation
- Lazy evaluation
- Job completion tracking in the History Server

Jobs can be submitted using:

```bash
/opt/spark/bin/spark-submit test.py

