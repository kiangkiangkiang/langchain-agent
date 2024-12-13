from flask import Flask, request, jsonify
from agent.agent.cathay_agent import CathayAgent
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


@app.route("/text_ask", methods=["POST"])
def text_ask():
    # 獲取 JSON 輸入
    agent = CathayAgent()
    data = request.get_json()

    # 確保鍵 'input' 存在
    if "input" not in data:
        return jsonify({"error": 'Missing "input" key in JSON data'}), 400

    # input_text = data["input"]

    output_text = agent(data)

    print(output_text)

    breakpoint()

    # 這裡可以填寫你的處理邏輯
    # 示例：假設處理邏輯是將輸入轉換成大寫
    # output_text = input_text.upper()

    # 返回 JSON 輸出
    return jsonify({"output": output_text})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
