import os
import json

from typing import Any



class Json_:	
    def path(name: str, ex: str = "json"):
        return os.path.abspath(__file__).replace(os.path.basename(__file__), f"{name}.{ex}")

    def read(name: str, default = None):
        path = Json_.path(name)

        if os.path.exists(path):
            with open(path, "r", encoding = "utf8") as f:
                return json.load(f)
        return default

    def write(name: str, data: Any):
        path = Json_.path(name)

        with open(path, "w", encoding = "utf8") as f:
            json.dump(data, f, indent = 4, ensure_ascii = False)
