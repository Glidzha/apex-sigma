import hashlib
import discord


async def gravatar(cmd, message, args):
    try:
        await cmd.bot.delete_message(message)
    except:
        cmd.log.error('Couldn\'t delete the gravatar image calling message.')
        pass
    if args:
        email = args[0]
        email = email.encode('utf-8')
        gravatar_url = "https://www.gravatar.com/avatar/" + hashlib.md5(email.lower()).hexdigest()
        embed = discord.Embed(color=message.author.color)
        embed.set_image(url=gravatar_url)
        await cmd.bot.send_message(message.channel, None, embed=embed)
    else:
        await cmd.bot.send_message(message.channel, cmd.help())
        return
