from telethon import Button

from userbot import BOTLOG, BOTLOG_CHATID, LOGS, tgbot


async def startupmessage():
    """
    Start up message in telegram logger group
    """
    try:
        if BOTLOG:
            await tgbot.send_file(
                BOTLOG_CHATID,
                "https://telegra.ph/file/6eb4e56da6eacfd4d6eef.jpg",
                caption="**Grovy Userbot Actived**⚡\n━━━━━━━━━━━━━━━\n➠ **Userbot Version** - 3.1.0@master\n━━━━━━━━━━━━━━━\n➠ **Powered By:** @GrovyUpdates ",
                buttons=[(Button.url("ꜱᴜᴘᴘᴏʀᴛ", "https://t.me/GrovySupport"),)],
            )
    except Exception as e:
        LOGS.error(e)
        return None
