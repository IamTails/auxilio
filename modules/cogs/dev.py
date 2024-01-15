from discord.ext import commands

from utilities.helpers import generate_embed


class Dev(commands.Cog):
    """Developer commands"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="test", description="test stuff")
    async def lol(self, ctx):
        embed = await generate_embed(ctx)
        embed.title = "Comprehensive Embed"
        name = "Test command Uwu"
        embed.set_author(name=name)
        embed.description = "This is a comprehensive example of Discord.py embed options."
        embed.set_thumbnail(
            url=ctx.author.display_avatar.with_static_format("png"))

        # Add fields to the embed
        embed.add_field(name="Field 1", value="Value 1", inline=True)
        embed.add_field(name="Field 2", value="Value 2", inline=True)
        embed.add_field(name="Field 3", value="Value 3", inline=False)
        embed.add_field(name="Field 4", value="Value 4", inline=False)
        embed.add_field(name="Field 5", value="Value 5", inline=False)

        # Add an inline field
        embed.add_field(name="Inline Field",
                        value="This field is inline.", inline=True)

        # Set an image for the embed
        embed.set_image(
            url=ctx.author.display_avatar.with_static_format("png"))

        # Add more fields
        embed.add_field(name="Field 6", value="Value 6", inline=True)
        embed.add_field(name="Field 7", value="Value 7", inline=True)
        embed.add_field(name="Field 8", value="Value 8", inline=False)
        # Send the embed
        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Dev(bot))
