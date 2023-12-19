import logging

from aiogram.types      import Message
from aiogram.utils 		import executor
from aiogram.dispatcher import Dispatcher, FSMContext

from Accest.gpt import ChatGPT

from Bot.bot import Bot_

from config import Config


class Main:
	async def start(message: Message, state: FSMContext):
		await Bot_.send_chat_action(message.chat.id, "typing", message.message_thread_id)
		text = ChatGPT.create(message.text)
		await Bot_(message).reply(text)

	async def on_startup(_):
		ChatGPT.set_promt_from_file()

		await Bot_.send_message(Config.CREATOR_ID, "Бот запущен")

		Bot_.me = await Bot_.bot.get_me()
		Bot_.id = Bot_.me.id
		Bot_.username = Bot_.me.username


	async def on_shutdown(dp: Dispatcher):
		logging.warning('Shutting down..')

		await Bot_.send_message(Config.CREATOR_ID, "Бот Выключен")

		logging.warning('Bye!')

	def main():
		executor.start_polling(
			dispatcher   = Bot_.dp,
			skip_updates = True,
			on_startup   = Main.on_startup,
			on_shutdown  = Main.on_shutdown,
			timeout		 = Bot_.timeout,
		)


if __name__ == '__main__':
    Main.main()
