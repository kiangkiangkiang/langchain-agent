from cathay_agent import CathayAgent
from customize_tools import *
from langchain_community.agent_toolkits.load_tools import load_tools


class AgentTemplate:
    @staticmethod
    def get_toy_agent():
        langchain_tools = load_tools(["requests_all"], allow_dangerous_tools=True)

        tools = [
            get_current_time,
            response_the_question_about_seating_chart,
        ]

        tools.extend(langchain_tools)
        prompt_store_name = "default"
        llm_store_name = "default"
        return CathayAgent.from_store(
            tools=tools,
            prompt_store_name=prompt_store_name,
            llm_store_name=llm_store_name,
        )


# agent = AgentTemplate.get_toy_agent()
# print(
#     agent(
#         {
#             "input": "你知道https://python.langchain.com/docs/tutorials/agents/裡面在說什麼嗎"
#         }
#     )
# )
