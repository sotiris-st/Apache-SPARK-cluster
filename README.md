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

```

---

## Spark History Server and Event Logs

The **Spark History Server** is enabled to provide visibility into completed Spark applications.

To support this, Spark event logging is configured via `spark-defaults.conf` and backed by an external Docker volume mounted at:

```
/tmp/spark-events
```

This allows the History Server to read Spark application logs even after jobs have completed or containers have been restarted.

---

## Volume Initialization and Permissions

A dedicated container named **`spark-init`** is used during cluster startup.

### Purpose of `spark-init`

Docker volumes are created with **root ownership by default**.  
Since Spark processes run as the `spark` user, this can lead to permission issues when Spark attempts to write event logs.

The `spark-init` container:

- Creates required directories such as `/tmp/spark-events` and `/tmp/spark-jobs`
- Sets correct ownership and permissions for the `spark` user
- Exits once initialization is complete

You can verify the directory permissions inside a container using:

```bash
ls -ld /tmp/spark-events
```

Expected output:

```
drwxr-xr-x 2 spark spark
```

This confirms that the `spark` user has read and write access to the directory.

---

## How to Run (Spark Standalone)

Start the cluster:

```bash
docker compose up -d
```

Verify containers are running:

```bash
docker ps
```

Submit the example job from the Spark master container:

```bash
docker exec -it spark-master /opt/spark/bin/spark-submit /tmp/spark-jobs/test.py
```

(Optional) view Spark UIs:

- Spark Master UI: `http://localhost:8080`
- Spark History Server UI: `http://localhost:18080`

---

## What This Demonstrates

- Spark Master–Worker architecture
- Client-mode Spark job submission
- Spark History Server configuration
- Persistent Spark event logging
- Docker-based Spark deployments
- Correct handling of Docker volume permissions

---

## Next Stage

The next stage extends the standalone Spark setup by introducing:

- **Apache Airflow**
- **SparkSubmitOperator**
- **PostgreSQL** as the Airflow metadata database
- **MinIO** as an S3-compatible object storage service

This enables orchestration of Spark jobs through Airflow while continuing to use the same standalone Spark cluster.


