import random


async def unflip_control(ev, message, args):
    if '(╯°□°）╯︵ ┻━┻' in message.content:
        if ev.db.get_settings(message.server.id, 'Unflip'):
            table = ['┬─┬ ノ( ^_^ノ)',
                     '┬─┬ ﾉ(° -°ﾉ)',
                     '┬─┬ ノ(゜-゜ノ)',
                     '┬─┬ ノ(ಠ\_ಠノ)',
                     '┻━┻~~~~  ╯(°□° ╯)',
                     '┻━┻====  ╯(°□° ╯)',
                     '┣ﾍ(^▽^ﾍ)Ξ(ﾟ▽ﾟ*)ﾉ┳━┳ There we go~♪',
                     ' ┬──┬﻿ ¯\_(ツ)',
                     '(ヘ･_･)ヘ┳━┳',
                     'ヘ(´° □°)ヘ┳━┳',
                     '┣ﾍ(≧∇≦ﾍ)… (≧∇≦)/┳━┳']
            ev.db.add_stats('TableCount')
            await ev.bot.send_message(message.channel, random.choice(table))
