import discord
import random

token = 'ODk2ODgyNTgxNDg2ODQxOTE3.YWNk_g.d6xol14ZYyYmZ5c4yX47HGAbptI'

client = discord.Client()

@client.event

async def on_ready():
    print('we have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')


    if message.author == client.user:
        return

    if message.channel.name == 'general':
        if user_message.lower() == 'hello doge':
            await message.channel.send(f'HEY!! {username}!')
            return
        elif user_message.lower() == 'yo doge':
            await message.channel.send(f'HEY!! {username}!')
            return
        elif user_message.lower() == 'bye doge':
            await message.channel.send(f'GOODBYE!! :( {username}!')
            return
        elif user_message.lower() == 'cya doge':
            await message.channel.send(f'GOODBYE!! :( {username}!')
            return
        elif user_message.lower() == '-doge':
            response = f'this is your random number: {random.randrange(1000000)}'
            await message.channel.send(response)
            return
        elif user_message.lower() == 'love you doge':
            await message.channel.send(f'i love you too :D! Never give up in life your worth it {username}.')
            return

client.run(token)

import discord
from discord.ext import commands
import youtube_dl

class music(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.command()
    async def join(ctx):
        if ctx.author.voice is None:
            await ctx.send("you're not is a vc please join one!")
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client.connect is None:
            await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)

    @commands.command()
    async def discconnect(self, ctx):
        await ctx.voice_client.disconnect()

        @commands.command()
        async def play(self,ctx,url):
            ctx.voice_client.stop()
            FFMPEG_OPTIONS = {'before_options':'-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
            YDL_OPTIONS = {'format':"bestaudio"}
            vc = ctx.voice_client

            with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
                info = ydl.extract_info(url, download=False)
                url2 = info['formats'][0]['url']
                source = await discord.FFmpegAudio.from_probe(url2, **FFMPEG_OPTIONS)
                vc.play(source)

                @commands.command()
                async def pause(self, ctx):
                    await ctx.voice_client.paused()
                    await ctx.send("paused")

                    @commands.command()
                    async def resume(self, ctx):
                        await ctx.voice_client.resume()
                        await ctx.send("resume")

    def setup(client):
         client.add_cog(music(client))

import discord
from discord.ext import commands
import music

cogs = [music]

client = commands.Bot(command_prefix='/', intents = discord.intents.all())
intents = discord.Intents.all()

for i in range(len(cogs)):
    cogs[i].setup(client)


    client.run("ODk2ODgyNTgxNDg2ODQxOTE3.YWNk_g.d6xol14ZYyYmZ5c4yX47HGAbptI")


client.run(token)
