from dotenv import load_dotenv
from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.playground import Playground, serve_playground_app
from phi.storage.agent.sqlite import SqlAgentStorage

from customize_toolkit import AdministrativeToolkit, RestaurantToolkit

load_dotenv()

administrative_agent = Agent(
    name="Administrative Agent",
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[AdministrativeToolkit()],
    storage=SqlAgentStorage(
        table_name="administrative_agent", db_file="administrative_agent.db"
    ),
    instructions=["專門回答行政相關事項的助手"],
    add_history_to_messages=True,
    markdown=True,
)

restaurant_agent = Agent(
    name="Restaurant Agent",
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[RestaurantToolkit()],
    storage=SqlAgentStorage(
        table_name="restaurant_agent", db_file="restaurant_agent.db"
    ),
    instructions=[
        "專門回答餐廳相關事項的助手，並且提供適時的推薦，注意，你可以反問使用者一些他想吃的想法，取得你要的推薦要素，再根據名單推薦。"
    ],
    add_history_to_messages=True,
    markdown=True,
)

pm_agent = Agent(
    team=[administrative_agent, restaurant_agent],
    model=OpenAIChat(id="gpt-4o-mini"),
    instructions=[
        "你是個專業的專案管理者，擅長溝通，協調等問題，使用者會問你很多問題，你可以視情況來交給你的成員，或是自行回答。"
    ],
    show_tool_calls=True,
    add_history_to_messages=True,
    markdown=True,
)

app = Playground(agents=[pm_agent]).get_app()


if __name__ == "__main__":
    serve_playground_app("cathay_agent:app", reload=True)
