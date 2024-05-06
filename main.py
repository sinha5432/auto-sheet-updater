
# 6fadce0fbe0d3be98e6fef69b03194b24abb982592438d3c037b61c5f917bdb7e618ac4dd36f4ada334e078600c30756516fe5769a0a2b514b4d417f1bb75266d0fba1c1a0d61677d948aa3d75051cbe17b2bf497fdf36180363f78899e114d5ad0a12bed55aee2c8b3e49f521665a1fdebbe844e25f8aed4db0afa32eb4803442fbf0c97b25489d9cf4721818af3be2821fbdb4ab7b3925857188fce7d26f8d35

import discord

intents = discord.Intents.default()
intents.messages = True

client = discord.Client(intents = intents)
guild = discord.Guild


print("Bot started")
@client.event
async def on_message(message):
    
    channelIDsToListen = ['bot-rolls'] # put the channels that you want to listen to here

    if message.channel.id in channelIDsToListen:

        if message.content != "" :
            print("New message: " + message.content)
    
client.run('6fadce0fbe0d3be98e6fef69b03194b24abb982592438d3c037b61c5f917bdb7e618ac4dd36f4ada334e078600c30756516fe5769a0a2b514b4d417f1bb75266d0fba1c1a0d61677d948aa3d75051cbe17b2bf497fdf36180363f78899e114d5ad0a12bed55aee2c8b3e49f521665a1fdebbe844e25f8aed4db0afa32eb4803442fbf0c97b25489d9cf4721818af3be2821fbdb4ab7b3925857188fce7d26f8d35')