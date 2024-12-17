from dotenv import load_dotenv

from agent.agent.agent_template import AgentTemplate

load_dotenv()


def text_ask():
    # 獲取 JSON 輸入
    agent = AgentTemplate.get_toy_agent()

    # input_text = data["input"]
    inputs = {"input": "你好，你知道王小明的位置嗎"}

    output_text = agent(inputs)

    return output_text["output"]


if __name__ == "__main__":
    print(text_ask())
