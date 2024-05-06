import discord
# permission -integer: 68608
# Discord bot token
TOKEN = 'TOKEN'

# ID of the server and channel you want to read messages from
SERVER_ID = 123
CHANNEL_ID = 123

# Message to display
DISPLAY_MESSAGE = "Hello from the bot!"

# Initialize the bot
intents = discord.Intents.default()
intents.messages = True  # Enable the message intent
intents.message_content = True # Enable message texts
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

    messages = []
    
    channel = client.get_channel(CHANNEL_ID)

    async for message in channel.history(limit=5):
        messages.append(message)

    # Display another message after reading all the previous messages
    # await channel.send(DISPLAY_MESSAGE)

 

    # Print all the previous messages

    for message in messages:
        print(f"{message.author}: {message.content}")


# Run the bot
client.run(TOKEN)