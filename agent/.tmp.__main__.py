from flask import Flask, request, jsonify
from agent.agent.agent_template import AgentTemplate
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


@app.route("/text_ask", methods=["POST"])
def text_ask():
    # 獲取 JSON 輸入
    agent = AgentTemplate.get_toy_agent()
    data = request.get_json()

    # 確保鍵 'input' 存在
    if "input" not in data:
        return jsonify({"error": 'Missing "input" key in JSON data'}), 400

    # input_text = data["input"]
    inputs = {"input": data['input']}

    output_text = agent(inputs)

    return jsonify({"output": output_text['output']})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
