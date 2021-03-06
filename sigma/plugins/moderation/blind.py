from sigma.core.permission import check_man_msg
from sigma.core.permission import check_man_roles
from sigma.core.permission import check_write
import discord


async def blind(cmd, message, args):
    channel = message.channel
    server = message.server
    if not message.mentions:
        await cmd.bot.send_message(message.channel, cmd.help())
        return
    user_q = message.mentions[0]
    overwrite = discord.PermissionOverwrite()
    overwrite.read_messages = False
    if message.author is not user_q:
        if check_man_msg(message.author, channel) and check_man_roles(message.author, channel):
            for chan in server.channels:
                if not chan.is_default:
                    if str(chan.type).lower() == 'text':
                        if check_write(user_q, chan):
                            await cmd.bot.edit_channel_permissions(chan, user_q, overwrite)
            embed = discord.Embed(color=0x66CC66, title=':white_check_mark: ' + user_q.name + ' Was Blinded!')
            await cmd.bot.send_message(message.channel, None, embed=embed)
        else:
            out_content = discord.Embed(color=0xDB0000,
                                        title=':no_entry: Insufficient Permissions. Users with Ban permissions only.')
            await cmd.bot.send_message(message.channel, None, embed=out_content)
