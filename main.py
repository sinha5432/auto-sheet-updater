import discord
import re

# Discord bot token
TOKEN = 'T'

# ID of the server and channel you want to read messages from
SERVER_ID = 1219687915798663349
CHANNEL_ID = 1219689307829440562

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
    

    guild = await client.fetch_guild(SERVER_ID)

    f = open("ingested_messages.txt", "r")

    ingested_msg = f.read().split(',')

    f.close()

    for message in messages:
        summary_message = message.content
        message_id = str(message.id)

        
        
        if message_id not in ingested_msg:
            print('not found')
            ingested_msg.append(message_id)

            open("ingested_messages.txt", )



            player_tags = re.findall("<(.*)>", summary_message)
            
            for players in player_tags:
                player_id = int(players[1:])

                user = await guild.fetch_member(player_id)
                nickname = user.nick
                
                character_name = nickname.split('|')[1].strip()
                player_name = nickname.split('|')[2].strip()


                print(f'{character_name} : {player_name}')


    f = open("ingested_messages.txt", "w")
    f.write(",".join(ingested_msg)[1:])
    f.close()
    
    print('All messages are done, pls close the code')
    
    


# Run the bot
client.run(TOKEN)

