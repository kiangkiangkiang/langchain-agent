from agent.agent.cathay_agent import CathayAgent
from langchain.agents import load_tools


class AgentTemplate:
    @staticmethod
    def get_basic_agent():
        tools = load_tools(["llm-math"])
        return CathayAgent.from_tools(tools)


agent = AgentTemplate.get_basic_agent()
print(agent({"input": "告訴我二的七次方是多少"}))
