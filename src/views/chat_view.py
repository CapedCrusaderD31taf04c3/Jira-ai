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
from models.chat_model import ChatModel
from llama_idx.ai_llama import LlamaChatBotAI, LlamaCompletionAI
from logger.custom_logger import Logger


chat_router = APIRouter()


class ChatV1View:
    """
    """
    @chat_router.post("/chat/v1/")
    async def chat_bot_v1(chat_model: ChatModel):
        """
        """
        
        try:
            Logger.info(message="Asking AI", stage="START")
                
            answer_text = LlamaChatBotAI.ask_llama(question=chat_model.question)
            
            Logger.info(message="AI Replied", stage="END")
            Logger.info(message="AI Communicated Successfully")

            response =  {
                "message": "Success",
                "status": 200,
                "data": str(answer_text)
            }

        except Exception as e:  
            Logger.error(str(e))
            response = {
                "message": "ERROR",
                "status": 500,
                "data": str(e)
            }

        return response



class ChatV2View:
    """
    """
    @chat_router.post("/chat/v2/")
    async def chat_bot_v2(chat_model: ChatModel):
        """
        """
        
        try:
            Logger.info(message="Asking AI", stage="START")
                
            answer_text = LlamaCompletionAI.ask_llama(question=chat_model.question)
            
            Logger.info(message="AI Replied", stage="END")
            Logger.info(message="AI Communicated Successfully")

            response =  {
                "message": "Success",
                "status": 200,
                "data": str(answer_text)
            }

        except Exception as e:  
            Logger.error(str(e))
            response = {
                "message": "ERROR",
                "status": 500,
                "data": str(e)
            }

        return response
