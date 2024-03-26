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

from llama_index.core.llms import ChatMessage, MessageRole
from llama_index.core import ChatPromptTemplate, PromptTemplate

class PromptStrings:
    """
    """

    QA_PROMPT_STR = (
        "Context information is below.\n"
        "---------------------\n"
        "{context_str}\n"
        "---------------------\n"
        "Given the context information and not prior knowledge, "
        "answer the question: {query_str}\n"
    )

    REFINE_PROMPT_STR = (
        "We have the opportunity to refine the original answer "
        "(only if needed) with some more context below.\n"
        "------------\n"
        "{context_msg}\n"
        "------------\n"
        "Given the new context, refine the original answer to better "
        "answer the question: {query_str}. "
        "If the context isn't useful, output the original answer again.\n"
        "Original Answer: {existing_answer}"
    )

class CustomPrompt:
    """
    """

    # Text QA Prompt
    chat_text_qa_msgs = [
        ChatMessage(
            role=MessageRole.SYSTEM,
            content=(
                "Always answer the question, even if the context isn't helpful."
            ),
        ),
        ChatMessage(role=MessageRole.USER, content=PromptStrings.QA_PROMPT_STR),
    ]
    text_qa_template = ChatPromptTemplate(chat_text_qa_msgs)

    # Refine Prompt
    chat_refine_msgs = [
        ChatMessage(
            role=MessageRole.SYSTEM,
            content=(
                "Always answer the question, even if the context isn't helpful."
            ),
        ),
        ChatMessage(role=MessageRole.USER, content=PromptStrings.REFINE_PROMPT_STR),
    ]
    refine_template = ChatPromptTemplate(chat_refine_msgs)


class PromptPassage:
    """
    """

    text_qa_template_str = (
        "Context information is"
        " below.\n---------------------\n{context_str}\n---------------------\nUsing"
        " both the context information and also using your own knowledge, answer"
        " the question: {query_str}\nIf the context isn't helpful, you can also"
        " answer the question on your own.\n"
    )
    text_qa_template = PromptTemplate(text_qa_template_str)

    refine_template_str = (
        "The original question is as follows: {query_str}\nWe have provided an"
        " existing answer: {existing_answer}\nWe have the opportunity to refine"
        " the existing answer (only if needed) with some more context"
        " below.\n------------\n{context_msg}\n------------\nUsing both the new"
        " context and your own knowledge, update or repeat the existing answer.\n"
    )
    refine_template = PromptTemplate(refine_template_str)