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

from fastapi import APIRouter
from models.ticket_model import TicketModel
from jira_agent.post_comment import PostComment
from jira_agent.create_ticket import CreateTicket
from llama_idx.ai_llama import LlamaCompletionAI

from prompts.get_solution_ai_prmt import GET_SOLUTION_PROMPT
from prompts.create_stories_ai_prmt import CREATE_STORIES_FROM_EPIC_PROMPT

from logger.custom_logger import Logger

import json

ticket_router_v2 = APIRouter()


class TicketView:
    """
    """
    @ticket_router_v2.post("/ticket/v2/")
    async def prform_jira_operations(ticket: TicketModel):
        """
        """
        try: 

            Logger.info(message="Retrieving Ticket Information", stage="START")

            ticket_key = ticket.issue.get("key", None)
            ticket_summary = ticket.issue.get("fields", {}).get("summary", None)
            ticket_desc = ticket.issue.get("fields", {}).get("description", None)
            ticket_type = ticket.issue.get("fields", {}).get("issuetype", {}).get("namedValue", None)
            
            Logger.info(message="Retrieved Ticket Information", stage="END")

            if ticket_type == "Epic":

                Logger.info(message=f"Detected Ticket category : \"{ticket_type}\"")

                Logger.info(message="Preparing AI Query", stage="START")
                question = f"{CREATE_STORIES_FROM_EPIC_PROMPT} {ticket_summary}"
                Logger.info(message="AI Query Prepared", stage="END")
                Logger.info(message="AI Query Prepared Successfully")

                Logger.info(message="Asking AI", stage="START")
                
                answer_text = LlamaCompletionAI.ask_llama(question=question)
                
                Logger.info(message="AI Replied", stage="END")
                Logger.info(message="AI Communicated Successfully")


                Logger.info(message="Converting AI text Reponse", stage="START")
                answer = json.loads(answer_text.response)
                Logger.info(message="Convered AI Response", stage="END")
                Logger.info(message="AI Reply converted Successfully")

                Logger.info(message=f"{len(answer)} Tickets will be created")                

                Logger.info(message="Creating \"Story\" Type Tickets", stage="START")
                result = CreateTicket().create_tickets(
                    stories=answer,
                    parent_ticket_id=ticket_key
                    )
                Logger.info(message="Created \"Story\" Type Tickets", stage="END")
                Logger.info(message=f"{len(answer)} Tickets Created Successfully")
            else:

                Logger.info(message=f"Detected Ticket category : \"{ticket_type}\"")

                Logger.info(message="Preparing AI Query", stage="START")
                question = f"{GET_SOLUTION_PROMPT} {ticket_desc}"
                Logger.info(message="AI Query Prepared", stage="END")
                Logger.info(message="AI Query Prepared Successfully")

                Logger.info(message="Asking AI", stage="START")
                
                answer = LlamaCompletionAI.ask_llama(question)
                
                Logger.info(message="AI Replied", stage="END")
                Logger.info(message="AI Communicated Successfully")

                Logger.info(message=f"Posting Comment to {ticket_key}", stage="START")
                result = PostComment().post_comment(
                    ticket_id=ticket_key,
                    comment=answer.response
                )
                Logger.info(message=f"Comment Posted to {ticket_key}", stage="END")
                Logger.info(message=f"Commented to Ticket Successfully")

            Logger.info("Preparing Response", stage="START")
            response =  {
                "message": "Success",
                "status": 200,
                "data": str(result)
            }
            Logger.info("Response Prepared", stage="END")
        except Exception as e:  
            Logger.error(str(e))
            response = {
                "message": "ERROR",
                "status": 500,
                "data": str(e)
            }

        return response

