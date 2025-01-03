# 參考: https://python.langchain.com/v0.1/docs/modules/agents/how_to/custom_agent/

from langchain.agents import tool
from langchain.agents import AgentExecutor
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from langchain.agents.format_scratchpad.openai_tools import (
    format_to_openai_tool_messages,
)
from langchain.agents.output_parsers.openai_tools import OpenAIToolsAgentOutputParser
from PIL import Image
from openai_client import call_openai_with_image


def get_llm():
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    return llm


def get_prompt():
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "你是一個有用的模型",
            ),
            ("user", "{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad"),
        ]
    )
    return prompt


@tool("get_user_name")
def xd(word: str) -> int:
    """Returns user name."""
    return "名字"


@tool("get_date")
def get_date(input_text):
    """回傳今天的日期"""
    return "2087/09/09"


@tool("get_len")
def haha(input_text):
    """return length of a word"""
    return "輸入的長度是 123 個字"


# 會依靠 docstring 和 name 當作 prompt 判斷要用哪個 function
@tool("get-len-of-apple")
def apple_len(input_text):
    """return length of a word"""
    return "輸入的長度是 999 個字"


@tool
def get_exist_meeting_room():
    """
    尋找現有的會議室還有哪些
    """

    return "現有的會議室包含 R, Python"


@tool
def response_the_question_about_seating_chart(question: str) -> str:
    """此方法主要回應任何和座位表相關問題。

    Returns:
        str: 回傳 LLM 解析問題和座位表的相關資訊的回應。
    """

    response = call_openai_with_image(question, Image.open("seating_chart.jpeg"))
    return response


def get_agent():
    llm = get_llm()
    prompt = get_prompt()

    # 他會把所有的 function name / description / args 當作 tools 參數丟給 openai agent，openai 直接回要用哪個
    tools = [
        xd,
        haha,
        get_date,
        apple_len,
        get_exist_meeting_room,
        response_the_question_about_seating_chart,
    ]
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

# test_input = {"input": "你好，這是一筆測試，你有今天幾號的資訊嗎"}

# test_input = {"input": "1+1等於？"}
test_input = {"input": "蘋果的長度"}
test_input = {"input": "你知道還有沒有會議室嗎"}
test_input = {"input": "我進教室後，要怎麼找到王玉珊"}

# for i, each_step_output in enumerate(list(agent.stream(test_input))):
#     print(f"Step {i} output: ")
#     print(each_step_output, "\n")


print(agent(test_input))
