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
from typing import Union
from vector_db.db_transactions import VectorDBQueries
from models.ticket_model import TicketModel

from logger.custom_logger import Logger

import uuid

search_router = APIRouter()

class SearchView:
    """
    """
    @search_router.get("/search/{search_str}")
    async def search(search_str: Union[str, None] = None):
        """
        """
        try: 
            
            results = VectorDBQueries.search_query(
                query=[search_str],
                where=None,
                where_document={
                    "$contains": search_str
                }
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
    @search_router.post("/insert-ticket/")
    async def insert_ticket(ticket: TicketModel):
        """
        """
        try:
            result = VectorDBQueries.insert_query(
                ids=[str(uuid.uuid4())],
                documents=[str(ticket)]
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