from langchain.agents import tool
from datetime import datetime
from PIL import Image
from utils.openai_client import call_openai_with_image


@tool
def get_current_time():
    """這段程式會回傳當前的時間，若有任何使用需要跟當前時間有關的資訊，可以透過此方法取得。

    Returns:
        str: 當前時間
    """
    return datetime.now().isoformat()


@tool
def response_the_question_about_seating_chart(question: str) -> str:
    """此方法主要回應任何和座位表相關問題。

    Returns:
        str: 回傳 LLM 解析問題和座位表的相關資訊的回應。
    """

    response = call_openai_with_image(question, Image.open("seating_chart.jpeg"))
    return response
