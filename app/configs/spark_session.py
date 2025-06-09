from pyspark.sql import SparkSession
from app.configs.app_settings import settings

def get_spark():
    spark = (
        SparkSession.builder
        .appName(settings.spark_app_name)
        .config("spark.jars.packages", "com.datastax.spark:spark-cassandra-connector_2.12:3.4.0")
        .config("spark.cassandra.connection.host", settings.cassandra_host)
        .config("spark.cassandra.connection.port", settings.cassandra_port)
        .getOrCreate()
    )
    return spark
