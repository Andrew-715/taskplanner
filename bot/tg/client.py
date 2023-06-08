import requests

from bot.tg.dc import GetUpdatesResponse, \
    SendMessageResponse, FromMessageResponse, \
    ChatResponse, UpdatesSchema


class TgClient:
    def __init__(self, token):
        self.token = token

    def get_url(self, method: str):
        return f"https://api.telegram.org/bot{self.token}/{method}"

    def get_updates(self, offset: int = 0, timeout: int = 60) -> GetUpdatesResponse:
        response = requests.get(self.get_url(
            f'getUpdates?offset={offset}&timeout={timeout}&'
            f'allowed_updates=["update_id","message"]'
        ))
        print(response.json())

        offset = 0
        tg_client = TgClient("token")
        while True:
            res = tg_client.get_updates(offset=offset)
            for item in res.result:
                offset = item.update_id + 1
                print(item.message)

    def send_message(self, chat_id: int, text: str) -> SendMessageResponse:
        raise NotImplementedError

    def from_message(self, chat_id: int, text: str) -> FromMessageResponse:
        raise NotImplementedError

    def get_chat(self, chat_id: int) -> ChatResponse:
        raise NotImplementedError