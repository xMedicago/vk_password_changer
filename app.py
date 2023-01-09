import asyncio


async def main():
    from loader import bot, dp
    from handlers import vk
    import logging

    logging.basicConfig(level=logging.INFO)

    dp.include_router(vk.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
