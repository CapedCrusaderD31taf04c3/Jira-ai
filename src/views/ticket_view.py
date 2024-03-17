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
from jira_agent.post_comment import PostComment
from jira_agent.create_ticket import CreateTicket
from gen_ai.ai_openai import JiraAI
from prompts.get_solution_ai_prmt import GET_SOLUTION_PROMPT
from prompts.create_stories_ai_prmt import CREATE_STORIES_FROM_EPIC_PROMPT


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
        
        ticket_type = ticket.issue.get("fields", {}).get("issuetype", {}).get("namedValue", None)


        
        # Using WEBHOOK
        # result = PostCommentWBH().post_comment(
        #     ticket_id=ticket_key,
        #     comment=answer
        # )

        if ticket_type == "Epic":
            question = f"{CREATE_STORIES_FROM_EPIC_PROMPT} {ticket_summary}"
            result = CreateTicket().create_tickets(
                stories=answer,
                parent_ticket_id=ticket_key
                )
        
        else:
            
            question = f"{GET_SOLUTION_PROMPT} {ticket_desc}"

            answer = JiraAI.ask_openai(question, ticket_type=ticket_type)

            result = PostComment().post_comment(
                ticket_id=ticket_key,
                comment=answer
            )

        return {
            "message": "Success",
            "status": 200,
            "data": str(result)
        }