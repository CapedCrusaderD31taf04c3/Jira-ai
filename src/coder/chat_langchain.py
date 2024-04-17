



from langchain.memory import ChatMessageHistory
from langchain_openai import ChatOpenAI
from langchain.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder
)
from .coder_prompt import OpenAICoderPrompt

class ChatHistory:
    """
    """

    history = ChatMessageHistory()

    @classmethod
    def create(cls, docs):
        """
        """
        # Loading Prompt
        cls.history.add_message(OpenAICoderPrompt.PROMPT)
        cls.history.add_message(OpenAICoderPrompt.SOURCE_CODE_COMING_MSG)
        
        for doc in docs:
            source_code = (
                f"# file_location : {doc.metadata['source']}\n"
                f"#####\n{doc.page_content}"
            )

            cls.history.add_message(source_code)

        cls.history.add_message(OpenAICoderPrompt.SOURCE_CODE_ARRIVED_MSG)

        return cls.history


class ChatOpenAILangV1:
    """
    """

    llm = ChatOpenAI(
        model="gpt-3.5-turbo-0125", 
        temperature=0.8
    )

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are an Expert Software Engineer who writes bugfree, scalable code",
            ),
            MessagesPlaceholder(variable_name="history"),
            ("human", "{input}"),
        ]
    )

    chain = prompt | llm

    def ask_lang_openai(self, question, docs):
        """
        """

        response = self.chain.invoke(
            {
                "history": ChatHistory.create(docs=docs).messages,
                "input": f"{question}",
            }
        )

        return response 