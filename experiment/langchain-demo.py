from langchain.agents import load_tools, initialize_agent, tool
from langchain.agents import AgentType
from langchain.chat_models.azure_openai import AzureChatOpenAI


OPENAI_API_KEY = "yourkey"
OPENAI_DEPLOYMENT_NAME = "gpt-35-16k"
MODEL_NAME = "gpt-35-turbo-16k"
OPENAI_DEPLOYMENT_ENDPOINT = "https://japanopenai2023ironman.openai.azure.com/"
OPENAI_API_TYPE = "azure"
OPENAI_API_VERSION = "2023-03-15-preview"


def get_llm_model():

    return AzureChatOpenAI(
        openai_api_key=OPENAI_API_KEY,
        openai_api_base=OPENAI_DEPLOYMENT_ENDPOINT,
        openai_api_type=OPENAI_API_TYPE,
        openai_api_version=OPENAI_API_VERSION,
        deployment_name=OPENAI_DEPLOYMENT_NAME,
        model_name=MODEL_NAME,
        temperature=0,
    )


def get_agent_buildin_tool(llm):
    tools = load_tools(["llm-math", "wikipedia"], llm=llm)
    return initialize_agent(
        tools,
        llm,
        agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,
        handle_parsing_errors=True,
        verbose=True,
    )


if __name__ == "__main__":
    llm = get_llm_model()
    agent = get_agent_buildin_tool(llm)

    print(agent("請幫我找到告五人的資訊"))
    print(agent("請問一百的四分之三是多少"))
