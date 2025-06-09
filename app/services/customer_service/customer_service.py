from pyspark.sql import SparkSession, DataFrame
from app.configs.app_settings import settings
from app.dtos.responses.base_response import BaseResponse
from pyspark.sql import functions as F

def process_customer_annual_salary(spark: SparkSession) -> BaseResponse[list[dict]]:
    try:
        df: DataFrame = (
            spark.read
            .format("org.apache.spark.sql.cassandra")
            .options(table=settings.cassandra_table, keyspace=settings.cassandra_keyspace)
            .load()
        )

        df_transformed = df.withColumn("annual_salary", df.salary * 12)
        result = df_transformed.toPandas().to_dict(orient="records")

        return BaseResponse(
            status_code=200,
            message="Customer data processed successfully",
            data=result
        )
    except Exception as e:
        return BaseResponse(
            status_code=500,
            message=f"Error processing customer data: {str(e)}",
            data=None
        )

def process_grouped_average_salary(spark: SparkSession) -> BaseResponse[list[dict]]:
    try:
        df: DataFrame = (
            spark.read
            .format("org.apache.spark.sql.cassandra")
            .options(table=settings.cassandra_table, keyspace=settings.cassandra_keyspace)
            .load()
        )

        df_grouped = (
            df.groupBy("last_name")
            .agg(F.avg("salary").alias("avg_salary"))
        )

        result = df_grouped.toPandas().to_dict(orient="records")

        return BaseResponse(
            status_code=200,
            message="Grouped average salary calculated successfully",
            data=result
        )
    except Exception as e:
        return BaseResponse(
            status_code=500,
            message=f"Error calculating grouped average salary: {str(e)}",
            data=None
        )