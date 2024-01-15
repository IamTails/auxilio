import datetime

import discord

from utilities.utilities import generate_embed_color


async def generate_embed(ctx):
    color = await generate_embed_color(ctx.author)
    em = discord.Embed(color=color)
    em.set_author(
        name="Auxilio",
        icon_url=ctx.bot.user.display_avatar.with_static_format("png"),
        url="https://discord.gg/invite/auxilio")
    timestamp = datetime.datetime.now(datetime.timezone.utc).strftime('%I:%M %p')
    em.set_footer(
        text=f"Command ran by {ctx.author.display_name} at {timestamp}",
        icon_url=ctx.author.display_avatar.with_static_format("png"))
    return em
