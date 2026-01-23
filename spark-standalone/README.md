## Run the Spark standalone cluster

Start the cluster:

```bash
docker compose up -d
```

Verify that containers are running:

```bash
docker ps
```

---

## Run a sample PySpark job

Enter the **Spark master** container:

```bash
docker exec -it spark-master bash
```

Create a job inside `/tmp/spark-jobs` (**this path is backed by a Docker volume**, so files persist across restarts):

```bash
cd /tmp/spark-jobs
touch test.py
cat > test.py
```

Paste the code from `sample.py`, then press **Ctrl + D** to save.

Submit the job to the Spark master:

```bash
/opt/spark/bin/spark-submit  test.py
```

You should see execution logs in the terminal.

---

## Spark UIs

- **Spark Master UI**: `http://localhost:8080`
 (workers and running applications)
- **Spark History Server UI**: `http://localhost:18080`
 (completed applications and event logs)

## Spark configuration

The standalone cluster uses a `spark-defaults.conf` file to set Spark defaults for job submission and observability.

### Master 

- `spark.master spark://spark-master:7077`
Sets the default Spark master URL for submissions, pointing to the standalone Spark master container.

### History Server and event logs

These settings enable Spark event logging so the **Spark History Server** can display completed applications:

- `spark.eventLog.enabled true`
Enables writing Spark event logs.

- `spark.eventLog.dir file:///tmp/spark-events`
Location where Spark writes event logs. In this project it is backed by a Docker volume for persistence.

- `spark.history.fs.logDirectory file:///tmp/spark-events`
Location the History Server reads from same directory as \`spark\.eventLog\.dir\`.

- `spark.eventLog.compress true`
Compresses event logs to save space.

### Executors 

These settings control how many executors Spark requests and how much resources they get:

- `spark.executor.instances 2`
Requests 2 executors 

- `spark.executor.cores 1`
Allocates 1 CPU core per executor.

- `spark.executor.memory 1g`
Allocates 1 GB of heap memory per executor.

- `spark.executor.memoryOverhead 256m`
Allocates additional off-heap memory per executor 


### Spark UI reverse proxy 

- `spark.ui.reverseProxy true`
Enables reverse-proxy support for Spark UI links.

- `spark.ui.reverseProxyUrl http://localhost:8080\`

Base URL used when Spark builds UI links behind a proxy. This can be helpful when accessing Spark UI through a forwarded or proxied address.
