# Copyright (C) 2024 CapedCrusaderD31taf04c3 <https://github.com/CapedCrusaderD31taf04c3>

# This program is not a free software: you can not redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# 
# =========================================================================================

from fastapi import APIRouter, status
from models.ticket_model import TicketModel
from webhooks.post_comment import PostCommentWBH
from jira_agent.post_comment import PostComment
from jira_agent.create_ticket import CreateTicket
from gen_ai.ai_openai import JiraAI
from prompts.get_solution_ai_prmt import GET_SOLUTION_PROMPT
from prompts.create_stories_ai_prmt import CREATE_STORIES_FROM_EPIC_PROMPT
import json

ticket_router = APIRouter()


class TicketView:
    """
    """
    @ticket_router.post("/ticket/")
    async def get_ticket_info(ticket: TicketModel):
        """
        """
        try: 
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
                answer_text = JiraAI.ask_openai(question, ticket_type=ticket_type)
                answer = json.loads(answer_text)
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

            response =  {
                "message": "Success",
                "status": 200,
                "data": str(result)
            }

        except Exception as e:  
            
            response = {
                "message": "ERROR",
                "status": 500,
                "data": str(e)
            }

        return response