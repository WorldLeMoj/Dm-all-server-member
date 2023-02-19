import discord
import os

intents = discord.Intents.default()
intents.members = True

bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

    # Get the server object by ID
    server = bot.get_guild(<SERVER_ID>)
    
    # Iterate over all members and send a message to each one
    for member in server.members:
        try:
            await member.send("<YOUR_MESSAGE>")
            print(f"Sent message to {member.name}#{member.discriminator}")
        except discord.errors.Forbidden:
            print(f"Couldn't send message to {member.name}#{member.discriminator}: missing permissions")

bot.run(os.environ['DISCORD_TOKEN'])
