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
from jira_agent.update_ticket import UpdateTicket
from llama_idx.ai_llama import LlamaCompletionAI, LlamaCompletionAIV2
from prompts.get_solution_ai_prmt import SolutionPMT
from prompts.create_stories_ai_prmt import CreateStoriesOpenAIPMT
from prompts.get_rca_and_solution_for_bugfix import RCAAndSolutionPMT
from logger.custom_logger import Logger
from helpers.ticket_info_extractor import TicketInfoExtractor

import json

ticket_router_v2 = APIRouter()


class TicketV2View:
    """
    """
    @ticket_router_v2.post("/v2/ticket/epic/")
    async def create_stories_from_epic_v2(ticket: TicketModel):
        """
        """
        try: 

            extract = TicketInfoExtractor(ticket)
            Logger.info(message=f"Detected Ticket category : \"{extract.ticket_type}\"")
            
            Logger.info(message="Preparing AI Query", stage="START")
            question = (
                f"{CreateStoriesOpenAIPMT.PROMPT}"
                "Q:{"
                f""" "heading": "{extract.ticket_summary}" """
                f""" "info" : "{extract.ticket_desc}" """
                "}"
                "A:"
            )
            Logger.info(message="AI Query Prepared", stage="END")
            Logger.info(message="AI Query Prepared Successfully")

            answer_text = LlamaCompletionAIV2.ask_llama(question=question)
            Logger.info(message="AI Communicated Successfully")

            result = CreateTicket().create_tickets(
                stories_text=answer_text.response,
                parent_ticket_id=extract.ticket_key
            )

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
            

    @ticket_router_v2.post("/v2/ticket/story/")
    async def comment_on_story_v2(ticket: TicketModel):
        """
        """
        try: 

            extract = TicketInfoExtractor(ticket)
            Logger.info(message=f"Detected Ticket category : \"{extract.ticket_type}\"")
            
            Logger.info(message="Preparing AI Query", stage="START")
            question = (
                f"{SolutionPMT.PROMPT}\n"
                f""" "title": "{extract.ticket_summary}" ,\n"""
                f""" "description": "{extract.ticket_desc}" """
            )
            Logger.info(message="AI Query Prepared", stage="END")
            Logger.info(message="AI Query Prepared Successfully")

            answer = LlamaCompletionAI.ask_llama(question)
            Logger.info(message="AI Communicated Successfully")

            result = PostComment().post_comment(
                ticket_id=extract.ticket_key,
                comment=answer.response
            )
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
    

    @ticket_router_v2.post("/v2/ticket/bug/")
    async def comment_on_bugfix_ticket_v2(ticket: TicketModel):
        """
        """
        try: 

            extract = TicketInfoExtractor(ticket)
            Logger.info(message=f"Detected Ticket category : \"{extract.ticket_type}\"")
            
            Logger.info(message="Preparing AI Query", stage="START")
            question = (
                f"{RCAAndSolutionPMT.PROMPT} "
                f"{extract.ticket_summary}:{extract.ticket_desc}"
            )
            Logger.info(message="AI Query Prepared", stage="END")
            Logger.info(message="AI Query Prepared Successfully")

            answer_text = LlamaCompletionAI.ask_llama(question)
            answer = json.loads(answer_text.response)
            Logger.info(message="AI Communicated Successfully")

            result = PostComment().post_comment(
                ticket_id=extract.ticket_key,
                comment=answer["solution"]
            )
            Logger.info(message=f"Commented to Ticket Successfully")

            if answer.get("root_cause", None):
                UpdateTicket().update_rca(
                    ticket_id=extract.ticket_key,
                    rca=answer["root_cause"]
                )
                Logger.info(message=f"RCA Updated to Ticket Successfully")

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

