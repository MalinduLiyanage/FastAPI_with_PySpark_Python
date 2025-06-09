from pydantic import BaseModel

class CustomerAnnualSalaryDTO(BaseModel):
    customer_id: str
    first_name: str
    last_name: str
    salary: float
    annual_salary: float

