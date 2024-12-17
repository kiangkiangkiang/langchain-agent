from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from agent.agent.base_store import BaseStore, registry_items, STORE_ITEMS


class PromptStore(BaseStore):
    store_name = "prompt"

    @registry_items(store_name, "default")
    def get_default_prompt():
        return ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "你是一個有用的模型",
                ),
                ("user", "{input}"),
                MessagesPlaceholder(variable_name="agent_scratchpad"),
            ]
        )
