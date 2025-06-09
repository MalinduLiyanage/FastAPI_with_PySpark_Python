from pydantic import BaseModel

class GroupedAverageSalaryDTO(BaseModel):
    last_name: str
    avg_salary: float
