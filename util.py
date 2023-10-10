import discord
from discord.ext import commands
import settings

class Memes:

    @staticmethod
    async def lookForApproval(message: discord.Message, b: commands.Bot):
        if message.attachments == []:
            return "No attachments were found in your message! Please send another message with an attachment. *Note that if you sent an attachment with a link, it will not work. Try uploading an attachment instead.*"
        else:
            f = await message.attachments[0].to_file()
            c = b.get_guild(settings.Config.guildid).get_channel(settings.Config.channelidtopostapprovalnotificationsto)
            if c.type == discord.ChannelType.forum or c.type == discord.ChannelType.text:
                await c.create_thread(name=message.author.display_name, content=f"Submitted by {message.author.mention}\n❔ Awaiting response...", file=f)
                return "# Your meme has been submitted!\n**Please allow up to 48 hours for staff to approve your meme.**\nYou'll be pinged in the channel when it is. If you don't receive a ping, your meme was most likely denied."
            else:
                raise Exception("Not a valid channel type!")
            
    @staticmethod
    async def approve(message: discord.Message, b: commands.Bot):
        if message.type == discord.MessageType.reply:
            f = await message.reference.resolved.attachments[0].to_file()
            c = b.get_guild(settings.Config.guildid).get_channel(settings.Config.channelidtopostapprovedmemesto)
            m = message.reference.resolved.content.split('\n')[0]
            await c.send(content=m + f"\nApproved by ||{message.author.mention}||", file=f)
            return await message.reference.resolved.edit(content=m + "\n✅ Approved!")