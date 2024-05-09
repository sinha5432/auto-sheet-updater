# Code is messed up currently
# Need help in editing to readable format XD

import discord
import re
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials


# Discord bot token
TOKEN = 't'

# ID of the server and channel you want to read messages from
SERVER_ID = 1219687915798663349
CHANNEL_ID = 1219689307829440562

MESSAGES_TO_FETCH = 1
SERVER_LEVEL_CAP = [4, 8]



# Initialize the bot
intents = discord.Intents.default()
intents.messages = True  # Enable the message intent
intents.message_content = True # Enable message texts
client = discord.Client(intents=intents)


# Define the scope
google_scope = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]


creds = Credentials.from_service_account_file('credentials.json', scopes=google_scope)

google_client = gspread.authorize(creds)
sheet = google_client.open('Tales of Exandria: Character levels').sheet1

data = sheet.get_all_records()
levels_df = pd.DataFrame(data)

def calculate_lvl(relevant_games: int) -> int:
    '''
    Level to get to   Games to play    Total
     2              2                0
     3              3                3
     4              5                8
     5              5                13
     6              10               23
    '''


    if relevant_games >=23:
        return 6

    if relevant_games >= 13:
        return 5

    if relevant_games >= 8:
        return 4
    
    if relevant_games >= 3:
        return 3
    
    return 2
    


@client.event
async def on_ready():
    print(f'INITIALISING AS {client.user}')

    messages = []
    
    channel = client.get_channel(CHANNEL_ID)

    async for message in channel.history(limit=MESSAGES_TO_FETCH):
        messages.append(message)


    guild = await client.fetch_guild(SERVER_ID)

    f = open("ingested_messages.txt", "r")

    ingested_msg = f.read().split(',')

    f.close()

    for message in messages:
        summary_message = message.content
        message_id = str(message.id)

        
        if message_id not in ingested_msg:
            print('NEW SUMMARY DETECTED, PARSING....')
            ingested_msg.append(message_id)

            player_tags = re.findall("<(.*)>", summary_message)
            
            for players in player_tags:
                player_id = int(players[1:])

                user = await guild.fetch_member(player_id)
                nickname = user.nick
                
                character_name = nickname.split('|')[1].strip()
                player_name = nickname.split('|')[-1].strip()

                if character_name not in levels_df['Character'].to_list():
                    num_of_characters = len(levels_df.index)
                    levels_df.loc[num_of_characters] = [num_of_characters, character_name, player_name, 1, 1, 2]
                else:

                    player_index = levels_df.index[levels_df.Character == character_name]
                    
                    total_games_played = levels_df.loc[player_index, 'Total-Games-Played' ].astype(int).iloc[0] + 1

                    if total_games_played >= SERVER_LEVEL_CAP[1]:
                        relevant_games = SERVER_LEVEL_CAP[1]
                    else:
                        relevant_games = total_games_played


                    current_lvl = calculate_lvl(relevant_games)


                    # converting all values to str coz due to some reason int wasn't getting updated
                    
                    levels_df.loc[player_index, 'Total-Games-Played' ] = str(total_games_played)
                    levels_df.loc[player_index, 'Games-Counted'] = str(relevant_games)

                    levels_df.loc[player_index, 'Current-Level' ] = str(current_lvl)
                    

                    sheet.update([levels_df.columns.values.tolist()] + levels_df.values.tolist())
                

    print(levels_df)


    f = open("ingested_messages.txt", "w")
    f.write(",".join(ingested_msg)[1:])
    f.close()
    
    print('All messages are done, pls close the code')
    
    


# Run the bot
client.run(TOKEN)

