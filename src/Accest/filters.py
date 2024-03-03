
from aiogram import types

from Bot.bot import Bot_

from Data.db           import DB
from Data.query.select import SELECT

from config import Config



class Filters:
    def is_teg_bot(message: types.Message) -> bool:
        res = Bot_.username in message.text or\
            Config.СHAT_GPT_BOT_NAME.lower() in message.text.lower() or (
                message.reply_to_message is not None and\
                message.reply_to_message.from_user.id == Bot_.id
            )

        return res

    def is_private(message: types.Message) -> bool:
        return message.chat.type == types.ChatType.PRIVATE

    def is_group(message: types.Message) -> bool:
        res = message.chat.type in (
            types.ChatType.GROUP,
            types.ChatType.SUPERGROUP,
        ) and message.chat.id == Config.MAIN_GROUP_ID

        return res

    def is_admin(message: types.Message) -> bool:
        db = DB()
        db.execute(SELECT.admin, (message.from_user.id,))
        exist_ = db.fetchone()

        res = exist_ is not None or message.from_user.id in Config.OWNERS_ID

        return res

    def is_owner(message: types.Message) -> bool:
        return message.from_user.id in Config.OWNERS_ID
