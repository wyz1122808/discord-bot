import discord
from discord import app_commands
from discord.ext import commands

client = commands.Bot(command_prefix="!", intents = discord.Intents.all())

@client.event
async def on_ready():
    print("launched")
    try:
        synced = await client.tree.sync()
        print(f'synced {len(synced)} commands')
    except Exception as e:
        print(e)



@client.tree.command(name="hello")
async def hello(interaction: discord.Interaction):

    await interaction.response.send_message(f'hey {interaction.user.mention}')


client.run('MTA3NDc0NTEyMzA3OTk4NzIxMA.GiK4U1.Oj4JABhq-wAHNsum0qr-5XayinP33fe2EvALas')