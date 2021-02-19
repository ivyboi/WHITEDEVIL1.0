"""Emoji

Available Commands:

.emoji shrug

.emoji apple

.emoji :/

.emoji -_-"""


import asyncio

from userbot.utils import lightning_cmd


@borg.on(lightning_cmd(pattern=r"call"))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 3

    animation_ttl = range(0, 18)

    # input_str = event.pattern_match.group(1)

    # if input_str == "call":

    await event.edit("Calling")

    animation_chars = [
        "`Connecting To Telegram Headquarters...`",
        "`Call Connected.`",
        "`Telegram: bhai bhai bhai shashank ka bot hello sur kese ho`",
        "`Me: MST bsdkkk ek chomu ka ib suspend krwna h `",

        "`Telegram: kiss ramdi me itni himmat.`",
        "`wo ek ladkki h @sundar_ho_tum ek no kii ramdii h`  `or usne hamare bechare nobita (sasta ajjubhai)ko dhoka diya `",
        "`Telegram: sur don't take tention me us ramdii ki tg acc se uski nude pic nikalta huu or aapka send krta huu`",
        "`Me: bsdkk jitna bola h pehle wo kr` `or lawde... uski nude pic 4k me send krna😋😋..`",
        "`Telegram: ye koii puchne kii baat h clips bhii send kr dunga`",
        "`Me: thikk h` ` or jara jldii khara ho gya mera ",
        "`Telegram: okk sur`",
        "`Me: bsdkk call pr hii h tuu jldii pics or clip send kr`",
[

 v69.6.9.\nI Am Not Able To Fix It. If Possible, Please Help Fix The Bug.`",
        
       

    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 18])
