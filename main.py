import discord
from discord.ext import commands, tasks
from itertools import cycle
from dotenv import load_dotenv
import os
import json
from webserver import keep_alive

load_dotenv
bot_token=os.getenv("BOT_TOKEN")
api_key = os.getenv("API_KEY")

def get_prefix(client, message):
    with open('prefixes.json', 'r') as f:
        prefixes=json.load(f)

    return prefixes[str(message.guild.id)]

client=commands.Bot(command_prefix=get_prefix)
status=cycle(['Enforcing', 'Vorckea sus'])

@client.event
async def on_ready():
    change_status.start()
    client.apikey = api_key
    client.load_extension('cogs.api')

@tasks.loop(seconds=31536000)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

@client.event
async def on_guild_join(guild):
    print(f'joined {guild.name}')
    with open('prefixes.json', 'r') as f:
        prefixes=json.load(f)

    prefixes[str(guild.id)] = '!'

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@client.event
async def on_guild_remove(guild):
    with open('prefixes.json', 'r') as f:
        prefixes=json.load(f)
    
    prefixes.pop(str(guild.id))

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@client.command()
@commands.guild_only()
@commands.has_permissions(administrator=True)
async def prefix(ctx, prefix):
    with open('prefixes.json', 'r') as f:
        prefixes=json.load(f)
    
    prefixes[str(ctx.guild.id)] = prefix

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)
    await ctx.send(f'Prefix has been changed to: `{prefix}`')

@client.command()
@commands.is_owner()
async def quit(ctx):
    await ctx.send("Shutting down the bot")
    await client.logout()

@client.command()
@commands.is_owner()
async def load(ctx, extension):
    if ctx.author.id == 613793967871492131:
        client.load_extension(f'cogs.{extension}')
        print(f'{extension} has been loaded')
@client.command()
@commands.is_owner()
async def unload(ctx, extension):
    if ctx.author.id == 613793967871492131:
        client.unload_extension(f'cogs.{extension}')
        print(f'{extension} has been unloaded')
@client.command()
@commands.is_owner()
async def rload(ctx, extension):
    if ctx.author.id == 613793967871492131:
        client.unload_extension(f'cogs.{extension}')
        await ctx.send(f'{extension} has been unloaded')
        client.load_extension(f'cogs.{extension}')
        await ctx.send(f'{extension} has been reloaded')

keep_alive()
client.run(bot_token)
