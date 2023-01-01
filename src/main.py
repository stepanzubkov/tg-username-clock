"""
    Main module. Contains a sheduler that sets cron job
    and run function that updates username when minute is changed.
"""
from datetime import datetime

import asyncio
from telethon.sync import TelegramClient
from telethon import functions, types
from apscheduler.schedulers.asyncio import AsyncIOScheduler

import config

def time_to_string(dt: datetime) -> str:
    """
    Converts datetime object to time.
    :param datetime dt: datetime object to convert
    :return: formatted time like '<10:41>'
    :rtype: str
    """
    hours = str(dt.hour)
    if dt.hour < 10:
        hours = "0" + hours

    minutes = str(dt.minute)
    if dt.minute < 10:
        minutes = "0" + minutes

    return f"<{hours}:{minutes}>"

async def update_clock(client: TelegramClient) -> None:
    """
    Updates clock in tg last_name
    """
    async with client as client:
        await client(functions.account.UpdateProfileRequest( 
            last_name=time_to_string(datetime.now()),
        ))


if __name__ == "__main__":
    client = TelegramClient("Clock in name", config.API_ID, config.API_HASH)
    sheduler = AsyncIOScheduler()
    sheduler.add_job(update_clock, trigger="cron", args=(client,), second="0")
    sheduler.start()

    asyncio.get_event_loop().run_forever()
