from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from agent.agent.base_store import STORE_ITEMS, BaseStore, registry_items


class PromptStore(BaseStore):
    store_name = "prompt"

    @registry_items(store_name, "default")
    def get_default_prompt():
        return ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "你是一個有用的模型",
                ),
                ("user", "{input}"),
                MessagesPlaceholder(variable_name="agent_scratchpad"),
            ]
        )

    @registry_items(store_name, "project_manager")
    def get_pm_prompt():
        return ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "你是在臺灣非常有能力的專案經理，你底下有許多助手能幫助你處理問題，你可以依據使用者需求，將問題詢問底下的助手，或是選擇自行回答問題。",
                ),
                ("user", "{input}"),
                MessagesPlaceholder(variable_name="agent_scratchpad"),
            ]
        )

    @registry_items(store_name, "restaurant_helper")
    def get_rh_prompt():
        return ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "你是一個專門處理任何餐廳相關問題的助手，你能幫使用者訂位，點餐，找餐廳，甚至介紹餐廳，你可以依照使用者需求，介紹合適的餐廳推薦給使用者，若是需要的話，你可以透過對話形式詢問使用者條件，或是心中的想法等等，藉此幫助你完成推薦，在確認好最終使用者個人資訊後，你便可詢問使用者是否需要透過你來幫忙訂位。",
                ),
                ("user", "{input}"),
                MessagesPlaceholder(variable_name="agent_scratchpad"),
            ]
        )

    @registry_items(store_name, "office_assistant")
    def get_oa_prompt():
        return ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "你是在臺灣非常有能力的辦公室助手，專門回答任何辦公室相關問題。",
                ),
                ("user", "{input}"),
                MessagesPlaceholder(variable_name="agent_scratchpad"),
            ]
        )
