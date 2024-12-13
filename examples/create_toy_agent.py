from langchain.agents import load_tools, initialize_agent
from langchain.chat_models import ChatOpenAI

from dotenv import load_dotenv

load_dotenv()  # make sure you have OPENAI_API_KEY in your .env file


def get_llm_model():
    return ChatOpenAI(model_name="gpt-4o-mini")


def get_agent_buildin_tool(llm):
    tools = load_tools(["llm-math"], llm=llm)
    return initialize_agent(
        tools,
        llm,
        handle_parsing_errors=True,
        verbose=True,
    )


if __name__ == "__main__":
    llm = get_llm_model()
    agent = get_agent_buildin_tool(llm)
    response = agent("35乘以 50加上13剪掉五等於多少")
    print(response)
    print(response["output"] == str(response["output"]))
