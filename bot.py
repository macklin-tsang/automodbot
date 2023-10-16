import discord
import responses

async def send_message(message, user_message):
    try:
        response = responses.handle_message(user_message)
        await message.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot():
    TOKEN = "MTE2MzMzMDI2NjI2NjM0NTU0NA.Gyzt7n.YwYbw_biAaFUmfRa0NEH3sBE0VgcfgbqwerCME"
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is running')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return 
        
        # if message.content.startswith('dirk'):
        #     await message.channel.send('quiet on ya block in some timbs when i lurk,\n glock shots got you on one foot fallin back like you Dirk')
        
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel.name)

        print(f"{username} said: '{user_message}' ({channel})")

        await send_message(message, user_message)
            

    client.run(TOKEN)