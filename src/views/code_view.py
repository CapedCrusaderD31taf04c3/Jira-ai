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
from helpers.ticket_info_extractor import TicketInfoExtractor
from logger.custom_logger import Logger
from coder.chat_langchain import ChatOpenAILangV1
from coder.code_updater import CodeUpdater

code_router = APIRouter()

class CodeView:
    """
    """
    @code_router.post("/code/")
    async def write_code(ticket: TicketModel):
        """
        """
        extract = TicketInfoExtractor(ticket)
        Logger.info(message=f"Detected Ticket category : \"{extract.ticket_type}\"")
        
        Logger.info(message="Preparing AI Query", stage="START")
        question = (
            "Q:{"
            f""" "heading": "{extract.ticket_summary}" """
            f""" "info" : "{extract.ticket_desc}" """
            "}"
            "A:"
        )

        

        answer = ChatOpenAILangV1.ask_lang_openai(question=question)  

        CodeUpdater(answer).update()

        response =  {
                "message": "Success",
                "status": 200,
                "data": answer
            }
        
        return response