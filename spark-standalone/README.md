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
