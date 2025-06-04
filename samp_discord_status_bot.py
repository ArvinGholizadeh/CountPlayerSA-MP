import discord
from discord.ext import commands, tasks
import asyncio
from samp_client.client import SampClient
import os

# --- Configuration - Load from Environment Variables ---
# Ensure these are set in your environment before running the bot.
# Example: export SERVER_IP="127.0.0.1"
SERVER_IP = os.getenv('SERVER_IP')
SERVER_PORT_STR = os.getenv('SERVER_PORT', '7777') # Default to 7777 if not set
BOT_TOKEN = os.getenv('BOT_TOKEN')

# Validate essential configuration
if not SERVER_IP:
    print("Error: SERVER_IP environment variable not set.")
    exit()
if not BOT_TOKEN:
    print("Error: BOT_TOKEN environment variable not set.")
    exit()

try:
    SERVER_PORT = int(SERVER_PORT_STR)
except ValueError:
    print(f"Error: Invalid SERVER_PORT "{SERVER_PORT_STR}". Must be an integer.")
    exit()

# --- Discord Bot Setup ---
intents = discord.Intents.default()
# No message_content intent needed if not processing messages.
# intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents) # Prefix not used if no commands defined

@tasks.loop(seconds=60.0)
async def update_server_status_task():
    """Periodically fetches SA-MP server info and updates the bot's Discord presence."""
    try:
        with SampClient(address=SERVER_IP, port=SERVER_PORT) as client:
            server_info = client.get_server_info()
            # The status message can be customized here.
            # For example, add emojis or change the wording.
            player_count_status = "Players: {players}/{max_players}".format(
                players=server_info.players,
                max_players=server_info.max_players
            )
            print(f"Updating status: {player_count_status}")
    except Exception as e:
        print(f"Error fetching server info: {e}")
        player_count_status = "Error fetching status" # Display error in status

    status_activity = discord.Activity(name=player_count_status, type=discord.ActivityType.watching)
    await bot.change_presence(status=discord.Status.do_not_disturb, activity=status_activity)

@bot.listen()
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    print(f'Monitoring SA-MP Server: {SERVER_IP}:{SERVER_PORT}')
    update_server_status_task.start() # Start the status update loop

# --- Run the Bot ---
if __name__ == "__main__":
    print("Starting bot...")
    bot.run(BOT_TOKEN)
