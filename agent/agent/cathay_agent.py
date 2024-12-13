from langchain_core.language_models.chat_models import BaseChatModel
from typing import List, Union
from langchain_core.tools.base import BaseTool
from langchain.agents import BaseSingleActionAgent, BaseMultiActionAgent
from langchain_core.runnables import Runnable
from langchain.agents import AgentExecutor
from langchain_core.prompts import BasePromptTemplate
from langchain.agents.format_scratchpad.openai_tools import (
    format_to_openai_tool_messages,
)
from langchain_openai import ChatOpenAI
from langchain.agents.output_parsers.openai_tools import OpenAIToolsAgentOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import BaseOutputParser


class CathayAgent:
    def __init__(
        self,
        tools: List[BaseTool],
        agent: Union[BaseSingleActionAgent, BaseMultiActionAgent, Runnable],
        **kwargs,
    ):

        self.agent_executor = AgentExecutor(
            agent=agent, tools=tools, verbose=True, **kwargs
        )

    def __call__(self, **inputs):
        return self.agent_executor(**inputs)

    @classmethod
    def from_tools(
        cls,
        tools: List[BaseTool],
        prompt: BasePromptTemplate = None,
        llm: BaseChatModel = None,
        output_parser: BaseOutputParser = None,
        **kwargs,
    ):

        llm = llm or ChatOpenAI(model="gpt-4o-mini", temperature=0)
        prompt = prompt or ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "你是一個有用的模型",
                ),
                ("user", "{input}"),
                MessagesPlaceholder(variable_name="agent_scratchpad"),
            ]
        )
        output_parser = output_parser or OpenAIToolsAgentOutputParser()

        llm_with_tools = llm.bind_tools(tools)

        agent = (
            {
                "input": lambda x: x["input"],
                "agent_scratchpad": lambda x: format_to_openai_tool_messages(
                    x["intermediate_steps"]
                ),
            }
            | prompt
            | llm_with_tools
            | output_parser
        )

        return cls(agent=agent, tools=tools, **kwargs)
