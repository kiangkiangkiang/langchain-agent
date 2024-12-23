from typing import List

from phi.model.content import Image
from phi.run.response import RunResponse
from phi.tools import Toolkit
from PIL import Image

from utils import call_openai_with_image


def get_registry_restaurant():
    return [
        "店名全家對麵，好吃程度5顆星，預約電話0912111222，地點台北市信義區三民路78號",
        "店名泰好吃，好吃程度4.8顆星，預約電話0229889888，地點台北市中正區中心路99號",
        "店名終魚下班了，好吃程度3.9顆星，預約電話0227887999，地點台北市松山區松山路12號",
        "店名口碑宮城獅，好吃程度4顆星，預約電話0912333445，地點台北市中山區可連路87號",
    ]


class AdministrativeToolkit(Toolkit):
    def __init__(self):
        super().__init__(name="administrative_toolkit")
        self.register(self.get_meeting_room_information)
        self.register(self.get_wifi_information)

    def get_meeting_room_information(self, meeting_room_question: str):
        """回答和會議室位置相關的所有資訊，只要使用者詢問和會議室、借會議室、會議室位置等等與會議室位置有關的任何問題可以將問題轉交給此方法以產生回應。

        Args:
            meeting_room_question (str): 與會議室相關的問題。

        Returns:
            str: 專業人士看過會議室地圖後，回答使用者問題的回應。
        """

        system_prompt = """
        你是一個專業的行政助理，你負責回答3樓會議室位置相關的所有資訊。

        你會得到一個3樓會議室位置圖以及和會議室相關的問題，請你使用此位置圖回答使用者問題。

        注意：
        1. 會議室位置圖內會有一些常見的程式語言名稱，例如 Java, Python，**這些名稱是會議室名稱**。
        2. **使用者並沒有圖的資訊**，因此你必須非常詳細具體描述使用者問題。

        若使用者詢問的資訊不在位置圖內，請你也好好跟使用者說明你無法回答。
        """

        response = call_openai_with_image(
            meeting_room_question,
            Image.open("./img/meeting_room_location.jpg"),
            system_prompt,
        )

        return response

    def get_wifi_information(self, wifi_question: str):
        """回答怎麼用wifi、取得wifi等相關訊息。

        Args:
            wifi_question (str): 與wifi相關的問題。

        Returns:
            str: 專業人士看過wifi介紹後，回答使用者問題的回應。
        """

        system_prompt = """
        你是一個專業的wifi使用者，你負責回答wifi相關訊息。

        你會得到一個wifi相關的使用手冊，請你使用此使用手冊回答使用者問題。

        注意：
        1. **使用者並沒有使用手冊的資訊**，因此你必須非常詳細具體回答使用者問題。

        若使用者詢問的資訊不在使用手冊內，請你也好好跟使用者說明你無法回答。
        """

        response = call_openai_with_image(
            wifi_question,
            Image.open("./img/wifi_guideline.jpg"),
            system_prompt,
        )

        return response


class RestaurantToolkit(Toolkit):
    def __init__(self):
        super().__init__(name="restaurant_agent")
        self.register(self.get_restaurant)

    def get_restaurant(self) -> str:
        """取得資料庫內所有已註冊的餐廳。

        Returns:
            str: 回傳所有資料庫已註冊的餐廳。
        """

        restaurant = get_registry_restaurant()  # return: List[str]

        restaurant = "\n".join([i for i in restaurant])

        return restaurant
