import discord
import random
from bot_logic import gen_pass
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.members = True  

bot = commands.Bot(command_prefix="/", intents=intents)


@bot.event
async def on_ready():
    print(f'Abbiamo fatto l\'accesso come {bot.user}')


@bot.event
async def on_member_join(member):
    guild = member.guild
    if guild.system_channel is not None:  
        to_send = f'Benvenuto {member.mention} in {guild.name}!'
        await guild.system_channel.send(to_send)


@bot.command()
async def pasw(ctx):
    await ctx.message.delete()  
    password = gen_pass(10)
    await ctx.send(f"La tua password generata è: `{password}`")


@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    await ctx.message.delete()  
    for i in range(times):
        await ctx.send(content)


@bot.command()
async def cfs(ctx, user_choice: str):
    await ctx.message.delete()  
    options = ['carta', 'forbice', 'sasso']
    if user_choice.lower() not in options:
        await ctx.send("Scelta non valida! Scrivi: carta, forbice o sasso.")
        return

    bot_choice = random.choice(options)
    await ctx.send(f"Tu hai scelto: {user_choice.capitalize()}")
    await ctx.send(f"Io ho scelto: {bot_choice.capitalize()}")

    if user_choice == bot_choice:
        result = "Pareggio! 🎲"
    elif (user_choice == 'carta' and bot_choice == 'sasso') or \
         (user_choice == 'forbice' and bot_choice == 'carta') or \
         (user_choice == 'sasso' and bot_choice == 'forbice'):
        result = "Hai vinto! 🎉"
    else:
        result = "Ho vinto io! 🤖"

    await ctx.send(result)


@bot.command()
async def helpme(ctx):
    await ctx.message.delete()  
    help_text = """
    **Lista comandi disponibili:**
    `/helpme` - Mostra questa lista di comandi.
    `/pasw` - Genera una password casuale.
    `/repeat <volte> <testo>` - Ripete il testo specificato per un certo numero di volte.
    `/cfs <carta/forbice/sasso>` - Gioca a carta, forbice, sasso contro il bot.
    """
    await ctx.send(help_text)


client.run("Insert token")
