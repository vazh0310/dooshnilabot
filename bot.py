from random import choice
import discord
import config

client = discord.Client()

def load_words():
    global words
    words = []
    
    try:
        f = open(config.wordsfile, 'r')

        ln = 0
        for line in f:
            words.append(line)
            ln += 1

        print(f"Loaded {ln} phrases")
    except FileNotFoundError:
        print(f"ERROR: File '{config.wordsfile}' not found!")
    finally:
        f.close()

def load_admwords():
    global admin_words
    admin_words = []
    
    try:
        f = open(config.admwordsfile, 'r')

        ln = 0
        for line in f:
            admin_words.append(line)
            ln += 1

        print(f"Loaded {ln} admin phrases")
    except FileNotFoundError:
        print(f"ERROR: File '{config.admwordsfile}' not found!")
    finally:
        f.close()
            
def load_dumbwords():
    global very_dumb_words
    very_dumb_words = []
    
    try:
        f = open(config.dumbwordsfile, 'r')

        ln = 0
        for line in f:
            very_dumb_words.append(line)
            ln += 1

        print(f"Loaded {ln} dumb phrases")
    except FileNotFoundError:
        print(f"ERROR: File '{config.dumbwordsfile}' not found!")
    finally:
        f.close()
        
@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):
    if ".dooshnila_exit" in message.content:
        if message.author.id in config.admins:
            embed = discord.Embed(title="Ладно.")
            await message.channel.send(content=None, embed=embed)
            exit(0)
        else:
            word = choice(admin_words)
            await message.channel.send(content=word)
    if message.author.id in very_stupid_id:
        word = choice(very_dumb_words)
        await message.channel.send(content=word)
    if message.author.id in idiots_id or message.content == ".dooshnila":
        word = choice(words)
        embed = discord.Embed(title="Режим душнилы активирован", description=word)
        await message.channel.send(content=None, embed=embed)

if __name__ == '__main__':
    client.run(config.token, bot=config.is_bot)
