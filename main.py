import discord
from discord.ext import commands
import settings
import util

def run():
    bot = commands.Bot(command_prefix="d.", intents=discord.Intents.all(), activity=settings.Config.a)

    @bot.event
    async def on_connect():
        print("Connected...")

    @bot.event
    async def on_ready():
        print("Ready!")

    @bot.event
    async def on_message(message: discord.Message):
        if message.author.bot == False:
            if message.channel.type == discord.ChannelType.private:
                response = await util.Memes.lookForApproval(message, bot)
                if response is None:
                    return await message.reply(content="An error occurred. Please try again.")
                else:
                    if response is not None:
                        return await message.reply(content=response)
            elif message.channel.type == discord.ChannelType.public_thread:
                if message.content == "||approve||":
                    await util.Memes.approve(message, bot)
                elif message.content == "||deny||":
                    await message.channel.delete()

    bot.run(settings.token)

if __name__ == "__main__":
    run()