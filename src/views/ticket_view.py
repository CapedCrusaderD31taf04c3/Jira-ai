from fastapi import APIRouter, status
from models.ticket_model import TicketModel

ticket_router = APIRouter()


class TicketView:
    """
    """
    @ticket_router.post("/ticket/")
    async def get_ticket_info(ticket_info: TicketModel):
        
        return {
                "message": "Success",
                "status": 200,
                "data": ticket_info.info
            }