import re

from aiogram            import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from .bot import Bot_

from Accest.translation.ttr import ttr
from Accest.translation.atr import atr
from Accest.translation.etr import etr
from Accest.translation.btr import btr
from Accest.gpt             import ChatGPT
from Accest.markups         import Markups

from Data.db           import DB
from Data.query.select import SELECT
from Data.query.insert import INSERT


class FormOwner(StatesGroup):
    change_promt = State()


class Owner:
    async def add_admin(message: types.Message, state: FSMContext):
        admin_id = int(re.match(r"/add[_ ](\d+)", message.text)[1])
        
        db = DB()
        db.execute(SELECT.admin, (admin_id,))
        exist_ = db.fetchone()
        if exist_ is not None:
            return await Bot_(message).answer(atr.t1)

        db.execute(INSERT.admins, (admin_id,))
        db.commit()

        await Bot_(message).answer(atr.t2)

    async def send_change_promt(message: types.Message, state: FSMContext):
        await Bot_(message).answer(ttr.t1, reply_markup = Markups.back)
        await FormOwner.change_promt.set()

    async def change_promt(message: types.Message, state: FSMContext):
        await state.finish()

        if message.text == btr.t1:
            return await Bot_(message).answer(ttr.t2.format(ChatGPT.get_promt()), reply_markup = Markups.empty)
        
        if ChatGPT.set_promt(message.text):
            return await Bot_(message).answer(ttr.t3.format(ChatGPT.get_promt()), reply_markup = Markups.empty)

        await Bot_(message).answer(etr.t1.format(ChatGPT.get_promt()), reply_markup = Markups.empty)
