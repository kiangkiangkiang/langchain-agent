from typing import List, Union
from langchain_core.tools.base import BaseTool
from langchain.agents import BaseSingleActionAgent, BaseMultiActionAgent
from langchain_core.runnables import Runnable
from langchain.agents import AgentExecutor
from langchain.agents.format_scratchpad.openai_tools import (
    format_to_openai_tool_messages,
)

from agent.agent.prompt_store import PromptStore
from agent.agent.llm_store import LLMStore


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

    def __call__(self, inputs, **kwargs):
        return self.agent_executor(inputs, **kwargs)

    @classmethod
    def from_store(
        cls,
        tools: List[BaseTool],
        prompt_store_name: str = "default",
        llm_store_name: str = "default",
        **kwargs,
    ):

        if (prompt := PromptStore.search(prompt_store_name)) is None:
            raise ValueError(f"Not Supported Prompt {prompt_store_name} in Cathay!")

        if (llm_obj := LLMStore.search(llm_store_name)) is None:
            raise ValueError(f"Not Supported LLM {llm_store_name} in Cathay!")

        llm, output_parser = llm_obj
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
