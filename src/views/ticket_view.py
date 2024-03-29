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
from prompts.get_solution_ai_prmt import GetSolutionOpenAIPMT
from prompts.create_stories_ai_prmt import CreateStoriesOpenAIPMT
from logger.custom_logger import Logger
from helpers.ticket_info_extractor import TicketInfoExtractor

ticket_router = APIRouter()


class TicketV1View:
    """
    """
    @ticket_router.post("/v1/ticket/epic/")
    async def create_stories_from_epic_v1(ticket: TicketModel):
        """
        """
        try: 

            extract = TicketInfoExtractor(ticket)
            Logger.info(message=f"Detected Ticket category : \"{extract.ticket_type}\"")
            
            Logger.info(message="Preparing AI Query", stage="START")
            question = (
                f"{CreateStoriesOpenAIPMT.CREATE_STORIES_FROM_EPIC_PROMPT} "
                f"{extract.ticket_summary} {extract.ticket_desc}"
            )
            Logger.info(message="AI Query Prepared", stage="END")
            Logger.info(message="AI Query Prepared Successfully")

            answer_text = JiraAI.ask_openai(question, ticket_type=extract.ticket_type)
            Logger.info(message="AI Communicated Successfully")
     
            result = CreateTicket().create_tickets(
                stories=answer_text,
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


    @ticket_router.post("/v1/ticket/story/")
    async def comment_on_story_v1(ticket: TicketModel):
        """
        """
        try: 

            extract = TicketInfoExtractor(ticket)
            Logger.info(message=f"Detected Ticket category : \"{extract.ticket_type}\"")
            
            Logger.info(message="Preparing AI Query", stage="START")
            question = (
                f"{GetSolutionOpenAIPMT.GET_SOLUTION_PROMPT} "
                f"{extract.ticket_summary} {extract.ticket_desc}"
            )
            Logger.info(message="AI Query Prepared", stage="END")
            Logger.info(message="AI Query Prepared Successfully")

            answer = JiraAI.ask_openai(question, ticket_type=extract.ticket_type)
            Logger.info(message="AI Communicated Successfully")
            
            result = PostComment().post_comment(
                ticket_id=extract.ticket_key,
                comment=answer
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