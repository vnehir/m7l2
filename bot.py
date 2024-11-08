import discord
from discord.ext import commands
from model import predict

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

# yeni bir komut 
# Dekaratör => Fonksiyona yeni özellikler ekleyerek fonksiyonu kontrol altına alır.
@bot.command()
async def kontrol(ctx):
#eğer kullanıcı fotoğraf gönderdiyse
    if ctx.message.attachments:
        for fotograf in ctx.message.attachments:
            file_name = fotograf.filename
            file_url = fotograf.url
            await fotograf.save(f'./img/{file_name}')
            await ctx.send(predict(imagePath= f'./img/{file_name}'))
    else:
        await ctx.send('Fotoğraf Göndermeyi Unuttunuz!')
    


bot.run("TOKEN")
