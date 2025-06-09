from pyspark.sql import SparkSession, DataFrame
from app.configs.app_settings import settings
from app.dtos.responses.base_response import BaseResponse

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
