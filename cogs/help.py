import discord
from discord.ext import commands
from discord import app_commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="help", description="Show all available AutoMod commands.")
    async def help_command(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="🛠️ AutoMod Help Menu",
            description="Here's a list of available commands for managing AutoMod settings.",
            color=discord.Color.teal()
        )

        embed.add_field(
            name="🔧 /setup",
            value="Interactively configure AutoMod using a UI with dropdowns, buttons, and selectors.",
            inline=False
        )

        embed.add_field(
            name="♻️ /force_update",
            value="Manually re-apply the active AutoMod preset to this server.",
            inline=False
        )

        embed.add_field(
            name="📋 /show_config",
            value="Display the currently active AutoMod configuration, including filters and exemptions.",
            inline=False
        )

        embed.add_field(
            name="🧹 /clear_config",
            value="Clear the current AutoMod settings for this server.",
            inline=False
        )

        embed.add_field(
            name="📢 /set_log_channel",
            value="Set which channel AutoMod should use for sending alerts and logs.",
            inline=False
        )

        embed.set_footer(text="Only members with Manage Server permission can use these commands.")
        embed.set_thumbnail(url=interaction.client.user.display_avatar.url)

        await interaction.response.send_message(embed=embed, ephemeral=True)

async def setup(bot):
    await bot.add_cog(Help(bot))
