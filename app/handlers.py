from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

router = Router()


@router.message(CommandStart)
async def cmd_start(message: Message):
    await message.answer('Добро пожаловать в бот Gemini AI by Google.')


@router.message()
async def ai(message: Message, state: FSMContext):
    pass
