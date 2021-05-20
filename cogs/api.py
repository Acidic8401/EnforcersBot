import discord
from discord.ext import commands
import aiohttp
import json
import embeds
import checks


class Api(commands.Cog):
    def __init__(self, client):
        self.client=client
        print(self.client.apikey)

    @commands.command()
    async def find(self, ctx, name):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://Enforcers.acidicfreerunni.repl.co/find/{name.lower()}/", ssl=False) as r:
                data = await r.json()
                try:
                    em=embeds.find(data["name"], bool(data["hacker"]), bool(data["crasher"]), bool(data["rwt"]), bool(data["tracker"]), bool(data["scammer"]))
                    await ctx.send(embed=em)
                except KeyError:
                    await ctx.send(f"Error! I couldn't find {name} in the database")


    @commands.command()
    @checks.isofficer()
    async def deepfind(self, ctx, name):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://Enforcers.acidicfreerunni.repl.co/deepfind/{name.lower()}/{str(self.client.apikey)}", ssl=False) as r:
                data = await r.json()
                try:
                    em=embeds.deepfind(data["name"], bool(data["hacker"]), bool(data["crasher"]), bool(data["rwt"]), bool(data["tracker"]), bool(data["scammer"]), data["proofurl"])
                    await ctx.send(embed=em)
                except KeyError:
                    await ctx.send(f"Error! I couldn't find {name} in the database")

def setup(client):
    client.add_cog(Api(client))