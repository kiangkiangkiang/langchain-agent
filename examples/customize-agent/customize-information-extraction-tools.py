# 參考: https://python.langchain.com/v0.1/docs/modules/agents/how_to/custom_agent/

from langchain.agents import tool
from langchain.agents import AgentExecutor
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from langchain.agents.format_scratchpad.openai_tools import (
    format_to_openai_tool_messages,
)
from langchain.agents.output_parsers.openai_tools import OpenAIToolsAgentOutputParser


def get_llm():
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    return llm


def get_prompt():
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "你是一個資訊擷取模型，你的任務是在一大段文字中擷取金融相關段落，並且一字不漏，不加油添醋的回傳給我。",
            ),
            ("user", "{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad"),
        ]
    )
    return prompt


@tool
def get_word_length(word: str) -> int:
    """Returns the length of a word."""
    return len(word)


def get_agent():
    llm = get_llm()
    prompt = get_prompt()
    tools = [get_word_length]
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
        | OpenAIToolsAgentOutputParser()
    )

    return AgentExecutor(agent=agent, tools=tools, verbose=True)


agent = get_agent()

news = """
近期，蘋果公司（Apple Inc.）發布了其最新季度的財報，顯示其營收超出市場預期，主要得益於iPhone銷量的增長。投資者對此反應積極，蘋果的股價在財報公布後強勢上漲。不過，市場分析師指出，未來的挑戰仍然存在，尤其是在全球供應鏈緊張和競爭加劇的情況下。

同時，在娛樂界，知名女演員詹妮弗·勞倫斯（Jennifer Lawrence）被拍到使用最新款的iPhone在好萊塢一家熱門餐廳拍攝照片。這一事件迅速引發熱議，許多粉絲讚揚她的品味，並好奇她是否會成為蘋果的下一位代言人。娛樂媒體也渲染了這一事件，猜測蘋果是否會利用這次免費的明星曝光增加其品牌影響力。

這種財務和娛樂事件的交織，顯示出科技產品在現代文化和生活中的重要地位，也讓人們更關注蘋果未來的產品策略和市場布局。
"""


print(list(agent.stream({"input": news})))
