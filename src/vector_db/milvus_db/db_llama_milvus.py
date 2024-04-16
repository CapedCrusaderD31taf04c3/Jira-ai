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
from llama_index.core import VectorStoreIndex, StorageContext, Document
from llama_index.vector_stores.milvus import MilvusVectorStore

class MilvusLlama:
    """
    Using llama_index for query engine and milvus db for storage context
    """

    # creates a milvus db collection if doesn't exists
    vector_store = MilvusVectorStore(dim=1536,collection_name="jira_tickets_llama",overwrite=False)
    storage_context = StorageContext.from_defaults(vector_store=vector_store)

    index = VectorStoreIndex.from_vector_store(vector_store=vector_store)

    @classmethod
    def insert_ticket(cls,json_data):

        ticket_id = json_data["issue"]["key"]
        doc = Document(text=str(json_data),doc_id=ticket_id)

        cls.index.insert(doc)

        return "Inserted Data"
    
    @classmethod
    def query_on_tickets(cls,user_query=None):

        query_engine = cls.index.as_query_engine()

        response = query_engine.query(user_query)
        return str(response)

