import os
import discord
from discord import app_commands
from discord.ext import commands

# Read token safely from Environment Variables
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

if not DISCORD_TOKEN:
    raise ValueError("Missing DISCORD_TOKEN environment variable!")

# Initialize Discord Bot
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    # Sync slash commands with Discord
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(f"Failed to sync commands: {e}")
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")


# Helper function to generate status embeds
def create_status_embed(user_display_name: str, avatar_url: str, action: str):
    embed = discord.Embed(
        title=f"⏳ {user_display_name} is {action}",
        description="**Don't interrupt!**",
        color=discord.Color.blue(),
    )
    embed.set_author(name=user_display_name, icon_url=avatar_url)
    return embed


# 1. /eat Command
@bot.tree.command(name="eat", description="Set status to afk eating")
async def eat(interaction: discord.Interaction):
    user = interaction.user
    embed = create_status_embed(user.display_name, user.display_avatar.url, "afk eating")
    await interaction.response.send_message(embed=embed)


# 2. /stdy Command
@bot.tree.command(name="stdy", description="Set status to studying")
async def stdy(interaction: discord.Interaction):
    user = interaction.user
    embed = create_status_embed(user.display_name, user.display_avatar.url, "studying")
    await interaction.response.send_message(embed=embed)


# 3. /slp Command
@bot.tree.command(name="slp", description="Set status to sleeping")
async def slp(interaction: discord.Interaction):
    user = interaction.user
    embed = create_status_embed(user.display_name, user.display_avatar.url, "sleeping")
    await interaction.response.send_message(embed=embed)


# Run the bot
bot.run(DISCORD_TOKEN)
