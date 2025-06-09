import uvicorn
from fastapi import FastAPI
from app.api.v1.endpoints import customer_endpoints
from app.configs.app_settings import settings

app = FastAPI(title="PySpark-Cassandra API")

app.include_router(customer_endpoints.router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run("app.main:app", host=settings.app_host, port=settings.app_port, reload=True)
