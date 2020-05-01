# @ayushk780
# Big Thanks To Spechide and @TechnoAyanBoT

"""Counth: Avaible commands: .hstat
"""

import asyncio
from telethon import events
from uniborg.util import admin_cmd, humanbytes, get_readable_time
import shutil


@borg.on(admin_cmd(pattern=r"hstat"))
async def _(event):
    if event.fwd_from:
        return
    
    total, used, free = shutil.disk_usage('.')
    total = humanbytes(total)
    used = humanbytes(used)
    free = humanbytes(free)
    stats = f'Total disk space: {total}\n' \
                        f'Used: {used}\n' \
                        f'Free: {free}'

    await event.edit(str(stats))
