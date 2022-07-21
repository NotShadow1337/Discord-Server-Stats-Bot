#libraries
import discord, json, asyncio
from discord.ext import commands, tasks

#intents (used to detect member joins)
intents = discord.Intents.default()
intents.members = True

#configuration
with open('config.json') as f:  config = json.load(f)

#client object
client = commands.Bot(command_prefix = 'z', case_insensitive = True, intents = intents)

#when the bot is ready to be used
@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    guild = client.get_guild(int(config['guild_id']))
    name = config['channel_name']
    new_name = config['channel_name'] + f' {len(guild.members)}'
    channel = client.get_channel(int(config['channel_id']))
    await channel.edit(name = new_name)
    await asyncio.sleep(int(config['delay']))

#when a member joins the server
@client.event
async def on_member_join(member):
    guild = client.get_guild(int(config['guild_id']))
    name = config['channel_name']
    new_name = config['channel_name'] + f' {len(guild.members)}'
    channel = client.get_channel(int(config['channel_id']))
    await channel.edit(name = new_name)

#when a member leaves the server
@client.event
async def on_member_remove(member):
    guild = client.get_guild(int(config['guild_id']))
    name = config['channel_name']
    new_name = config['channel_name'] + f' {len(guild.members)}'
    channel = client.get_channel(int(config['channel_id']))
    await channel.edit(name = new_name)

#logging in to the bot
client.run(config['token'])