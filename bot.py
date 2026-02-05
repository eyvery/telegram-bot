import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

TOKEN = "8472149967:AAGBMDFyVdrrEUR34yDpzgQvl079CMs_8Lo"
ADMIN_ID = 1581085110

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer(
        "Привет! ✉️\n"
        "Напиши сюда если спамблок. Вскоре отвечу."
    )


@dp.message()
async def forward_to_admin(message: types.Message):
    if message.from_user.id == ADMIN_ID:
        return

    text = (
        f"📩 Новое сообщение\n"
        f"От: @{message.from_user.username}\n"
        f"ID: {message.from_user.id}\n\n"
        f"{message.text}"
    )

    await bot.send_message(ADMIN_ID, text)
    await message.answer("✅ Отправлено!")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
