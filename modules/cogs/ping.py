import datetime
import discord
from discord.ext import commands

from utilities.helpers import generate_embed


class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(name="ping", description="Show bot and API latency.")
    @commands.guild_only()
    async def ping(self, ctx):
        embed = await generate_embed(ctx)
        embed.title = "Pong!"
        embed.description = f"Bot latency: {self.bot.latency * 1000:.2f} ms"
        await ctx.reply(embed=embed, mention_author=False)


async def setup(bot):
    await bot.add_cog(Ping(bot))
