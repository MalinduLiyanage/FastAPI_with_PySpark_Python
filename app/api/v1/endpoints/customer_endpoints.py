from fastapi import APIRouter, Depends
from typing import List, Any
from app.dtos.customer.annual_salary_DTO import CustomerAnnualSalaryDTO
from app.dtos.customer.average_salary_DTO import GroupedAverageSalaryDTO
from app.dtos.responses.base_response import BaseResponse
from app.services.customer_service.customer_service import process_customer_annual_salary, \
    process_grouped_average_salary
from app.configs.spark_session import get_spark

router = APIRouter()

@router.get("/process-annual-salary", response_model=BaseResponse[List[CustomerAnnualSalaryDTO]])
async def get_processed_customers(spark=Depends(get_spark)) -> Any:
    return process_customer_annual_salary(spark)

@router.get("/grouped-average-salary", response_model=BaseResponse[List[GroupedAverageSalaryDTO]])
async def get_grouped_average_salary(spark=Depends(get_spark)) -> Any:
    return process_grouped_average_salary(spark)