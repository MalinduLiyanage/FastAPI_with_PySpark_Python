from fastapi import APIRouter, Depends
from typing import List, Any
from app.dtos.customerDTO import CustomerAnnualSalaryDTO
from app.dtos.responses.base_response import BaseResponse
from app.services.customer_service.customer_service import process_customer_annual_salary
from app.configs.spark_session import get_spark

router = APIRouter()

@router.get("/process-annual-salary", response_model=BaseResponse[List[CustomerAnnualSalaryDTO]])
async def get_processed_customers(spark=Depends(get_spark)) -> Any:
    return process_customer_annual_salary(spark)
