from typing import Final
import os
from discord import Intents, client, Message
from responses import get_response
from dotenv import load_dotenv

load_dotenv()
TOKEN: Final[str] = os.getenv("DISCORD_TOKEN")

intents: Intents = Intents.default()
intents.message_content = True # NOQA
client = client.Client(intents=intents)


async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print("empty message")
        return


    try:
        response: str = get_response(user_message)
        await message.channel.send(response)
    except Exception as e:
        print(e)

@client.event
async def on_ready() -> None:
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message: Message):
    if message.author == client.user:
        return
    username: str = str(message.author)
    user_message: str = str(message.content)
    channel: str = str(message.channel)

    print(f"{username} said: '{user_message}' ({channel})")

    await send_message(message, user_message)


@client.event
async def on_message_edit(before: Message, after: Message):
    if before.author == client.user:
        return

    username: str = str(after.author)
    user_message: str = str(after.content)
    channel: str = str(after.channel)

    print(f"{username} edited the message to: '{user_message}' ({channel})")

    await send_message(after, user_message)

def main() -> None:
    client.run(token=TOKEN)

if __name__ == "__main__":
    main()