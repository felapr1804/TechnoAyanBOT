"""counth"""

from telethon import events

import asyncio
from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern=r"counth"))
async def _(event):
    if event.fwd_from:
        return

    animation_interval = 3

    animation_ttl = range(0, 100)

    # input_str = event.pattern_match.group(1)

    # if input_str == "hack":

    await event.edit("Printing count..")

    animation_chars = [k for k in range(100)]

    for i in animation_ttl:
        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 100])
