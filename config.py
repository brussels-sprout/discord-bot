TOKEN = None

bot = None


def set_bot():
    from discord.ext import commands

    global bot
    bot = commands.Bot(command_prefix="b!")


set_bot()
