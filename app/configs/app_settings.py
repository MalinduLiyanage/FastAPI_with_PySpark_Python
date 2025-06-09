import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="C:/Users/malin/PycharmProjects/PysparkFastAPI/.env")

print(os.getenv("CASSANDRA_HOST"))

class Settings:
    cassandra_host: str = os.getenv("CASSANDRA_HOST")
    cassandra_port: str = os.getenv("CASSANDRA_PORT")
    cassandra_keyspace: str = os.getenv("CASSANDRA_KEYSPACE")
    cassandra_table: str = os.getenv("CASSANDRA_TABLE")
    spark_app_name: str = os.getenv("SPARK_APP_NAME")
    app_host: str = os.getenv("API_HOST")
    app_port: int = os.getenv("API_PORT")

settings = Settings()


