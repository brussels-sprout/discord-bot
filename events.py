import config

import discord

bot = config.bot


@bot.event
async def on_ready():
    latency = round(bot.latency, 3) * 1000  # in ms to 3 d.p.

    for guild in bot.guilds:
        try:
            await guild.me.edit(nick=f"{bot.user.name} | {bot.command_prefix}")
        except discord.Forbidden:
            pass

    print(f"Connected successfully as {bot.user} ({latency}ms).")
