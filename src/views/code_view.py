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
from llama_idx.ai_llama import LlamaCompletionAIV2
from logger.custom_logger import Logger
from helpers.ticket_info_extractor import TicketInfoExtractor


code_router = APIRouter()

class CodeView:
    """
    """
    @code_router.post("/code/")
    async def write_code():
        """
        """
        question = """
        You're tasked with reviewing and modifying the codebase located in the src folder. 
        Begin by thoroughly understanding the code's structure, dependencies, and functionalities. 
        Implement the modifications ensuring alignment with best practices and maintaining readability. 
        For each file needing updates, provide the modifid only files by applying update in code text only,
        Test the modified code thoroughly to ensure proper functionality, 
        Upon completion, submit the updated codebase.
        so task is,
        suport new feature to add task category, input for the task will be name of the task category
        """
        answer_text = LlamaCompletionAIV2.ask_llama(question=question)

        response =  {
                "message": "Success",
                "status": 200,
                "data": answer_text
            }
        
        return response