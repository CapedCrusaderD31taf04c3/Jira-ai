from pydantic import BaseModel

class TicketModel(BaseModel):
    info: dict