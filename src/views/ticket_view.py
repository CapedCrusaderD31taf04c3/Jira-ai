# Copyright (c) 2024 CapedCrusader
# All rights reserved.
#
# This software is licensed under the terms of the MIT.
# You should have received a copy of the license along with this
# program. If not, see LICENSE File.
# 
# ======================================

from fastapi import APIRouter, status
from models.ticket_model import TicketModel

ticket_router = APIRouter()


class TicketView:
    """
    """
    @ticket_router.post("/ticket/")
    async def get_ticket_info(ticket: TicketModel):
        """
        """
        return {
            "message": "Success",
            "status": 200,
            "data": ticket
        }