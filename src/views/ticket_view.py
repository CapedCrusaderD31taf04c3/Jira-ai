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
from webhooks.post_comment import PostCommentWBH

from gen_ai.ai_openai import JiraAI

ticket_router = APIRouter()


class TicketView:
    """
    """
    @ticket_router.post("/ticket/")
    async def get_ticket_info(ticket: TicketModel):
        """
        """

        ticket_key = ticket.issue.get("key", None)
        
        ticket_summary = ticket.issue.get("fields", {}).get("summary", None)
        ticket_desc = ticket.issue.get("fields", {}).get("description", None)
        
        answer = JiraAI.ask_openai(ticket_desc)

        result = PostCommentWBH().post_comment(
            ticket_id=ticket_key,
            comment=answer
        )

        return {
            "message": "Success",
            "status": 200,
            "data": result
        }