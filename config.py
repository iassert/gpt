from aiogram.bot.api import TelegramAPIServer


class Config:
    TOKEN: str
    CREATOR_ID: int
    OWNERS_ID: list[int]  = [CREATOR_ID]

    MAIN_GROUP_ID: int

    LOCAL_SERVER:TelegramAPIServer  = TelegramAPIServer.from_base('http://localhost:8081')

    DATABASE: str = "gpt"
    USER:     str = "assert"
    PASSWORD: str = "KhERp2ni_ALpRMdv3paBJUG-hVOryTu0"
    HOST:     str
    PORT:     str = "5434"

    API_KEY: str

    СHAT_GPT_BOT_NAME: str
