import discord
from discord.ext import commands

def isofficer():
    def predicate(ctx):
        officer_role=ctx.guild.get_role(784133930554228783)
        return ctx.author.top_role >= officer_role
    return commands.check(predicate)
