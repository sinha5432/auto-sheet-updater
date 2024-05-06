import discord
import re

# Discord bot token
TOKEN = 'TOKEN'

# ID of the server and channel you want to read messages from
SERVER_ID = 'ID'
CHANNEL_ID = 'ID'

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

    async for message in channel.history(limit=1):
        messages.append(message)

    # Display another message after reading all the previous messages
    # await channel.send(DISPLAY_MESSAGE)
    
    # Print all the previous messages

    guild = await client.fetch_guild(SERVER_ID)



    for message in messages:
        summary_message = message.content

        # print(summary_message)

        player_tags = re.findall("<(.*)>", summary_message)
        
        for players in player_tags:
            player_id = int(players[1:])

            user = await guild.fetch_member(player_id)
            nickname = user.nick
            
            character_name = nickname.split('|')[1].strip()
            player_name = nickname.split('|')[2].strip()


            print(f'{character_name} : {player_name}')



    
    print('All messages are done, pls close the code')
    
    


# Run the bot
client.run(TOKEN)

