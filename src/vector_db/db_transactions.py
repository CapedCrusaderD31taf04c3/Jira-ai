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

from .db_connection import ChromaVectorDB

from logger.custom_logger import Logger

class VectorDBQueries:
    """
    """
    @classmethod
    def insert_query(cls, ids, documents):
        """
        """

        ChromaVectorDB.collection.add(
            ids=ids,
            documents=documents
        )

        return "Created"

    @classmethod
    def search_query(
            cls, query=None, where=None, where_document=None
        ):
        """
        """
        Logger.info(message="Searching In DB", stage="START")
        results = ChromaVectorDB.collection.query(
            query_texts=query,
            n_results=50,
            where=where,
            where_document=where_document
        )
        Logger.info(message="Search Operation Completed", stage="END")
        return results