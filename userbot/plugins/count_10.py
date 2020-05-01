# @ayushk780
# Big Thanks To Spechide & @TechnoAyanBoT

"""Counth: Avaible commands: .cten
"""

import asyncio
from telethon import events
from uniborg.util import admin_cmd



@borg.on(admin_cmd(pattern=r"cten"))
async def _(event):
    if event.fwd_from:
        return

    animation_interval = 0.3

    animation_ttl = range(0, 10)

    # input_str = event.pattern_match.group(1)

    # if input_str == "hack":

    await event.edit("Printing count..")

    animation_chars = [
    
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    '10',
    '11'
    
    ]

    for i in animation_ttl:
        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 10])
