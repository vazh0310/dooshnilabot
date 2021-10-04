from random import choice
import discord

client = discord.Client()

words = [
    "блять", "ты че долбоеб?", "ору", "иди нахуй", "ебанат", "еблан",
    "даун", "пиздец", "придурок", "уебан", "убейся об стенку аутист",
    "еблан тупорылый", "ебало представили?", "в чем я не прав?",
    "негры заебали", "за россию, сука!", "ты мудак или да?",
    "ой блядь началось...", "хуй соси", "пидор штоль?", "порвался?",
    "у тебя НЕ бомбит, верю", "говорят ты хуи сосешь, это правда?",
    "дегенерат", "хуйло", "ебаный козел", "черножопый даун", "конченый",
    "это мне?", "ебало завали", "оффнись нахуй, чмо"
]

very_dumb_words = [
    "я тебе все сказал", "повторять не собираюсь", "собака, собачья жизнь!",
    "тебя не спрашивали", "я больше не повторяю", "все детали были обговорены",
    "не надо тут ля-ля, уважаемый", "ну-ну, маня", "так сказать то что хотел?",
    "уведомляю вас о том, что я выставил вам требования", "порвался таки",
    "при выполнении указанных требований немецкое командование гарантирует вам \
    исключение из списка долбоебов"
]

admin_words = [
    "может мне еще и отсосать у тебя?", "бля, может сам офнешься?",
    "нахуй не здесь", "это мне?", "отъебись", "я за россию, а ты вижу пидераст!"
]

premsg = "Мне задали оскорблять тебя: "

idiots_id = [

]

very_stupid_id = [

]

admins = [
    557251333250351142
]

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if '.dooshnila_exit' in message.content:
        if message.author.id in admins:
            #await message.channel.send("Ладно.")
            embed = discord.Embed(title="Ладно.")
            await message.channel.send(content=None, embed=embed)
            exit()
        else:
            word = choice(admin_words)
            await message.channel.send(content=word)
    if message.author.id in very_stupid_id:
        word = choice(very_dumb_words)
        await message.channel.send(content=word)
    if message.author.id in idiots_id or message.content == ".dooshnila":
        word = choice(words)
        #await message.channel.send(f"{premsg} {word}")
        embed = discord.Embed(title="Режим душнилы активирован", description=word)
        await message.channel.send(content=None, embed=embed)

if __name__ == '__main__':
    client.run(token, bot=False)
