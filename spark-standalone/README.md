We can just set up the cluster with 
```
docker compose up
```
After the cluster is up we can then enter ths spark-master container as below
```
docker exec -it sparm-master bash
```
To run a spark job we have to create a .py file. We create it in /tmp/spark-jobs path. We see that the specific directory has been created since we have mounted in the exeternal volume spark-jobs in the docker-compose.yaml and has the permissions so as to be able to create files.

Inside the spark-jobs directory we can create the .py file as below 
```
touch test.py
cat > test.y
```
Then we copy the code from the sample.py file and press Ctrl + D. After this we just execute the test.py as below
```
/opt/spark/bin/spark-submit test.py
```
After this we will see the execution logs
In our browser if we visit localhost:8080 we will see that the application is running. After finishing we can see the application logs dags etc in spark-history server typing localhost:18080 in our browser.

Run the Spark standalone cluster

Start the cluster:

```bash
docker compose up -d
```

Verify that containers are running:

```bash
docker ps
```

Run a sample PySpark job

Enter the Spark master container:

```bash
docker exec -it spark-master bash
```

Create a job inside /tmp/spark-jobs (this path is backed by a Docker volume, so files persist across restarts):

```bash
cd /tmp/spark-jobs
touch test.py
cat > test.py
```

Paste the code from sample.py, then press Ctrl + D to save.

Submit the job to the Spark master:

```bash
/opt/spark/bin/spark-submit --master spark://spark-master:7077 test.py
```

You should see execution logs in the terminal.

Spark UIs

Spark Master UI: http://localhost:8080 (workers and running applications)

Spark History Server UI: http://localhost:18080 (completed applications and event logs)
