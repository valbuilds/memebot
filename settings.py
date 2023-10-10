from dotenv import load_dotenv
load_dotenv()
import os
import json
import discord


token: str = os.getenv('token')

class Config:
    f = open('config.json')
    json = json.load(f)

    channelidtopostapprovalnotificationsto: int = json['channel-id-to-post-approval-notifications-to']
    channelidtopostapprovedmemesto: int = json['channel-id-to-post-approved-memes-to']
    guildid: int = json['guild-id']
    a = discord.Activity(type=discord.ActivityType.custom, name=json['status'])