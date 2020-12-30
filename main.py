# Note: If you host the bot on Heroku (https://heroku.com/), you
# need to assign your Discord bot token to a Config Var named "TOKEN".

import setup
import events
import commands


def run_bot():
    from config import TOKEN, bot

    def modify_allowed_mentions():
        import discord

        nonlocal bot

        bot.allowed_mentions = discord.AllowedMentions(
            everyone=None,
            users=None,
            roles=None
        )

    modify_allowed_mentions()

    bot.run(TOKEN)


run_bot()
