import aiohttp
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")


"""
sample .env file

BOT_TOKEN=1234567890:ABCDEFG
CHAT_ID=123456789
"""


async def send_incident_notification(incident):
    if not BOT_TOKEN or not CHAT_ID:
        raise ValueError("BOT_TOKEN or CHAT_ID not set in .env")

    message = (
        f"🆘 Новый инцидент!\n\n"
        f"ID: {incident.id}\n"
        f"Описание: {incident.description}\n"
        f"Статус: {incident.status}\n"
        f"Источник: {incident.source}\n"
        f"Создано: {incident.created_at}"
    )

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    async with aiohttp.ClientSession() as session:
        await session.post(url, json={"chat_id": CHAT_ID, "text": message})

