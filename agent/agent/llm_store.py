from langchain_openai import ChatOpenAI
from langchain.agents.output_parsers.openai_tools import OpenAIToolsAgentOutputParser
from base_store import BaseStore, registry_items, STORE_ITEMS


class LLMStore(BaseStore):
    store_name = "llm"

    @registry_items(store_name, "default")
    def get_default_llm():
        return (
            ChatOpenAI(model="gpt-4o-mini", temperature=0),
            OpenAIToolsAgentOutputParser(),
        )
