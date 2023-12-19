from aiogram import types

from Accest.translation.ptr import ptr
from Accest.filters         import Filters

from Bot.bot    import Bot_
from Bot.owners import FormOwner, Owner

from Handlers.main import Main

Bot_.dp.register_message_handler(
    Owner.send_change_promt,
    Filters.is_owner,
    commands = "promt",
    state = "*"
)
Bot_.dp.register_message_handler(
    Owner.change_promt,
    Filters.is_owner,
    content_types = types.ContentTypes.TEXT,
    state = FormOwner.change_promt
)

Bot_.dp.register_message_handler(
    Owner.add_admin,
    Filters.is_owner,
    regexp = ptr.t1,
    content_types = types.ContentTypes.TEXT,
    state = "*"
)

Bot_.dp.register_message_handler(
    Main.start,
    Filters.is_owner,
    Filters.is_private,
    content_types = types.ContentTypes.TEXT,
    state = "*"
)

Bot_.dp.register_message_handler(
    Main.start,
    Filters.is_admin,
    Filters.is_group,
    Filters.is_teg_bot,
    content_types = types.ContentTypes.TEXT,
    state = "*"
)
