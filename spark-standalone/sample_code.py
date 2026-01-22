from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, upper

spark = SparkSession.builder \
    .appName("DataFrameCleaningAndJoinDemo") \
    .getOrCreate()

# -----------------------------
# Create DataFrame 1 (users)
# -----------------------------
users_data = [(i, f"user_{i}", 20 + (i % 10)) for i in range(1, 101)]
users_df = spark.createDataFrame(users_data, ["user_id", "name", "age"])

# Introduce some dirty data
users_df = users_df.withColumn(
    "age",
    when(col("user_id") % 15 == 0, None).otherwise(col("age"))
)

# -----------------------------
# Create DataFrame 2 (orders)
# -----------------------------
orders_data = [(i, i % 100 + 1, i * 10.5) for i in range(1, 101)]
orders_df = spark.createDataFrame(orders_data, ["order_id", "user_id", "amount"])

# Introduce some dirty data
orders_df = orders_df.withColumn(
    "amount",
    when(col("order_id") % 20 == 0, None).otherwise(col("amount"))
)

# -----------------------------
# Cleaning logic
# -----------------------------
clean_users_df = users_df.fillna({"age": 0}) \
    .withColumn("name", upper(col("name")))

clean_orders_df = orders_df.fillna({"amount": 0.0})

# -----------------------------
# Join logic
# -----------------------------
joined_df = clean_users_df.join(
    clean_orders_df,
    on="user_id",
    how="inner"
)

# -----------------------------
# Aggregation
# -----------------------------
result_df = joined_df.groupBy("user_id", "name", "age") \
    .sum("amount") \
    .withColumnRenamed("sum(amount)", "total_spent")

# Trigger execution
result_df.show(10)
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++Total rows:", result_df.count(),"+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++Number of partitions:", result_df.rdd.getNumPartitions(),"+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

