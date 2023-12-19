import os
import openai

from config import Config

from Accest.translation.atr import atr
from Accest.translation.ftr import ftr

from Log.log import Log

from Json.json_ import Json_


openai.api_key = Config.API_KEY

class ChatGPT:
    __log = Log("gpt")

    __promt: str = ""
    __messages = [
        {
            "role": "system", 
            "content": __promt
        }
    ]

    __limit = 940

    @staticmethod
    def create(text: str) -> str:
        out = ""

        for i in [
            text[i:i + ChatGPT.__limit] 
            for i in range(0, len(text), ChatGPT.__limit)
        ]:
            ChatGPT.__messages.append(
                {
                    "role": "user", 
                    "content": i
                }
            )

            try:
                request = openai.ChatCompletion.create(
                    model = "gpt-3.5-turbo-1106",
                    messages = ChatGPT.__messages,
                    max_tokens = ChatGPT.__limit // 2,
                    temperature = 1
                )

                msg = request.choices[-1].message["content"]

                ChatGPT.__messages.append(
                    {
                        "role": "assistant", 
                        "content": msg
                    }
                )

                out += msg
            except Exception as ex:
                ChatGPT.__log.error(ex)

        return out

    @staticmethod
    def set_promt_from_file() -> bool:
        path = Json_.path(ftr.promt, ftr.ex_txt)
        
        if not os.path.exists(path):
            return False
        
        try:
            with open(path, "r", encoding = "utf-8") as f:
                ChatGPT.__promt = f.read()
            return True
        except Exception as ex:
            ChatGPT.__log.error(ex)
        return False

    @staticmethod
    def get_promt() -> str:
        return ChatGPT.__promt

    @staticmethod
    def set_promt(promt: str) -> None:
        path = Json_.path(ftr.promt, ftr.ex_txt)

        try:
            with open(path, "w", encoding = "utf-8") as f:
                f.write(promt)
            ChatGPT.__promt = promt
            return True
        except Exception as ex:
            ChatGPT.__log.error(ex)
        return False
