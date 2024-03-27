import discord
import random
from settings import token
from bot_logic import gen_pass

# Zmienna intencje przechowuje uprawnienia bota
intents = discord.Intents.default()
# Włączanie uprawnienia do czytania wiadomości
intents.message_content = True
# Tworzenie bota w zmiennej klienta i przekazanie mu uprawnień
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Cześć!")
    elif message.content.startswith('$bye'):
        await message.channel.send("Pa!")
    elif message.content.startswith('$password'):
        await message.channel.send(gen_pass(10))
    elif message.content.startswith('$rzut monetą'):
        coin = random.randint(1,2)
        if coin == 1:
            await message.channel.send("Orzeł")
        elif coin == 2:
            await message.channel.send("Reszka")
    elif message.content.startswith('$rzut kością'):
        dice = random.randint(1,6)
        await message.channel.send(dice)
    elif message.content.startswith('$liczba od 1 do 10'):
        number = random.randint(1,10)
        await message.channel.send(number)
    else:
        await message.channel.send(message.content)

client.run(token['TOKEN'])
