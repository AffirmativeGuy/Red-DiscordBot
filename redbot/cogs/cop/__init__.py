from redbot.core.bot import Red
from .cop import cop
import json
from pathlib import Path



old_info = None
old_ping = None
old_invite = None

# Thanks to yami for making me understand this code
# I Will add the works of every line here in near future!
async def setup(bot: Red) -> None: 
    global old_invite
    global old_info
    global old_ping
    old_info = bot.get_command("info")
    old_ping = bot.get_command("ping")
    old_invite = bot.get_command("invite")
    if old_info:
        bot.remove_command(old_info.name)
    if old_ping:
        bot.remove_command(old_ping.name)
    if old_invite:
        bot.remove_command(old_invite.name)
    
    cog = cop(bot)
    await bot.add_cog(cog)

# Thanks to yami for making me understand this code
def teardown(bot: Red) -> None:
    global old_invite
    global old_info
    global old_ping
    if old_info:
        bot.remove_command("info")
        bot.add_command(old_info)
    if old_ping:
        bot.remove_command("ping")
        bot.add_command(old_ping)
    if old_invite:
        bot.remove_command("invite")
        bot.add_command(old_invite)
