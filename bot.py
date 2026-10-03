import discord
import os
import random
from discord.ext import commands

permisos = discord.Intents.default()
permisos.message_content = True

bot = commands.Bot(command_prefix="!", intents=permisos)

@bot.event
async def on_ready():
    print(f"el bot esta en linea {bot.user}")

@bot.command()
async def hola(ctx):
    await ctx.send(f"¿Hola bienvenido, en que te puedo ayudar hoy {ctx.author.name} ?")

#crear mas comandos
@bot.command()
async def ayuda(ctx):
    await ctx.send("Los comandos que existen son: !hola, !ayuda")

@bot.command()
async def cuentame_un_chiste(ctx):
    await ctx.send("¿Qué le dice un techo rico a un techo pobre? !te-echo de menos! 😄")

@bot.command()
async def cuentame_un_dato_curioso(ctx):
    await ctx.send("Sabias que las hormigas no duermen")

@bot.command()
async def muestrame_un_meme(ctx):
    imagenes = os.listdir("imagen")
    imagen_enviar = random.choice(imagenes)
    with open(f"imagen/{imagen_enviar}","rb") as f:
        picture = discord.File(f) 
    await ctx.send(file = picture)

bot.run = ("")
