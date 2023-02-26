# Pyspark 3.3.2 removed support for kafka. see:
# https://stackoverflow.com/questions/61891762/spark-3-x-integration-with-kafka-in-python

from pyspark.sql import SparkSession
import pyspark_streaming.config as config
from pyspark.sql.types import StringType, StructField, StructType
from pyspark.sql.functions import from_json, col

topic = "reviews"

spark = SparkSession \
    .builder \
    .appName("Streaming from Kafka") \
    .config("spark.streaming.stopGracefullyOnShutdown", True) \
    .config('spark.jars.packages', 'org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.2') \
    .config("spark.sql.shuffle.partitions", 4) \
    .master("local[*]") \
    .getOrCreate()

spark

# Create the streaming_df to read from kafka
streaming_df = spark.readStream\
    .format("kafka") \
    .option("subscribe", topic) \
    .option("kafka.bootstrap.servers", config.KAFKA_URL) \
    .option("kafka.sasl.mechanism", config.KAFKA_SASL_MECHANISM) \
    .option("kafka.security.protocol", config.KAFKA_SECURITY_PROTOCOL) \
    .option(
        "kafka.sasl.jaas.config",
        f"org.apache.kafka.common.security.scram.ScramLoginModule required username=\"{config.KAFKA_USERNAME}\" password=\"{config.KAFKA_PASSWORD}\";"
    ) \
    .option("startingOffsets", "earliest") \
    .load()

schema = StructType([
    StructField("value", StringType())
])

# Convert the "value" column from binary to string and parse the JSON
parsed_df = streaming_df \
    .select(from_json(col("value").cast("string"), schema).alias("json")) \
    .select("json.*")

# Select the "value" column and write it to a console
query = parsed_df \
    .select("value") \
    .writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

query.awaitTermination()