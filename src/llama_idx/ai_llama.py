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

from llama_index.core import (
    VectorStoreIndex, 
    SimpleDirectoryReader,
    StorageContext,
    load_index_from_storage
)

from .chat_promt import CustomPrompt, PromptPassage
import os


class DirLoader:
    """
    """

    
    doc_dir_path = os.getenv("PROJECT_DIR")
    PERSIST_DIR = os.getenv("STORE_INDEX_AT")

    if not os.path.exists(PERSIST_DIR):
        # load the documents and create the index
        
        documents = SimpleDirectoryReader(input_dir=doc_dir_path, recursive=True).load_data()
        index = VectorStoreIndex.from_documents(documents)
        # store it for later
        index.storage_context.persist(persist_dir=PERSIST_DIR)
    else:
        # load the existing index
        storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
        index = load_index_from_storage(storage_context)

class LlamaCompletionAI:
    """
    """

    query_engine = DirLoader.index.as_query_engine(
        text_qa_template=PromptPassage.text_qa_template,
        refine_template=PromptPassage.refine_template,
    )

    @classmethod
    def ask_llama(cls, question):
        """
        """

        answer = cls.query_engine.query(question)
        return answer


class LlamaChatBotAI:
    """
    """

    query_engine = DirLoader.index.as_query_engine(
        text_qa_template=CustomPrompt.text_qa_template,
        refine_template=CustomPrompt.refine_template,
    )

    @classmethod
    def ask_llama(cls, question):
        """
        """

        
        answer = cls.query_engine.query(question)
        return answer
