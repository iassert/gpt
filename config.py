from aiogram.bot.api import TelegramAPIServer


class Config:
    TOKEN: str = "6288904451:AAGzx3XAviy_AjKNVQ71WPR1UKJD2pzgzTw"
    CREATOR_ID: int = 704750195
    OWNERS_ID: list[int]  = [CREATOR_ID, 364156591]

    MAIN_GROUP_ID: int = -1001780886382

    LOCAL_SERVER: TelegramAPIServer = TelegramAPIServer.from_base('http://localhost:8081')

    DATABASE: str = "gpt"
    USER:     str = "assert"
    PASSWORD: str = "KhERp2ni_ALpRMdv3paBJUG-hVOryTu0"
    HOST:     str = "172.17.128.1"
    PORT:     str = "5434"

    API_KEY: str = "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"

    СHAT_GPT_BOT_NAME: str = "Влад"
