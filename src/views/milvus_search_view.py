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
from vector_db.milvus_db.db_llama_milvus import MilvusLlama
from models.ticket_model import TicketModel

from logger.custom_logger import Logger

milvus_search_router = APIRouter()

class SearchView:
    """
    """
    @milvus_search_router.get("/v2/search/{query}")
    async def search(query: str = ""):
        """
        """
        try: 
            results = MilvusLlama.query_on_tickets(
                user_query=query
            )

            return {
                "message": "Success",
                "status": 200,
                "data": {
                    "msg" : results
                }
            }
        
        except Exception as e:  
            Logger.error(str(e))
            response = {
                "message": "ERROR",
                "status": 500,
                "data": str(e)
            }

        return response
    

class InsertTicketInDBView:
    """
    """
    @milvus_search_router.post("/v2/insert-ticket/")
    async def insert_ticket(ticket: TicketModel):
        """
        """
        try:
            ticket_json = ticket.model_dump()
            result = MilvusLlama.insert_ticket(
                json_data=ticket_json
            )

            response =  {
                "message": "Success",
                "status": 200,
                "data": {
                    "msg" : result
                }
            }

        except Exception as e:  
            Logger.error(str(e))
            response = {
                "message": "ERROR",
                "status": 500,
                "data": str(e)
            }

        return response