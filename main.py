import discord
from discord.ext import commands
from python_weather import Client
import asyncio
from datetime import datetime
import pytz

intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")


@bot.command(name="enviar_imagem")
async def send_image(ctx):
    image_path = r"C:\Users\rande\PycharmProjects\wpp\fototeste.png"
    await ctx.send(file=discord.File(image_path))


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith("!iniciar"):
        name = message.author.name
        response = f"Olá, {name}, seja bem vindo ao RandBot"
        await message.channel.send(response)
    elif message.content.startswith("!clima"):
        await get_weather(message)


async def get_weather(message):
    await message.channel.send("Por favor, digite a cidade e o estado (formato: cidade, UF):")

    def check(m):
        return m.author == message.author and m.channel == message.channel

    try:
        response = await bot.wait_for("message", check=check, timeout=60)
        location = response.content

        weather_client = Client()
        weather = await obter_informacoes_meteorologicas(location, weather_client)

        br_timezone = pytz.timezone('America/Sao_Paulo')
        local_time_br = datetime.now(br_timezone).strftime('%d/%m/%Y %H:%M:%S')

        await message.channel.send(f"**Clima em {location}:**\n"
                                   f"Temperatura: {weather.temperature}°C\n"
                                   f"Sensação térmica: {weather.feels_like}°C\n"
                                   f"Umidade: {weather.humidity}%\n"
                                   f"Horário local: {local_time_br}")
    except asyncio.TimeoutError:
        await message.channel.send("Tempo limite expirado. Por favor, tente novamente.")


async def obter_informacoes_meteorologicas(location, weather_client):
    async with weather_client:
        weather = await weather_client.get(location)
        return weather


bot.run("SEU_TOKEN_AQUI")
