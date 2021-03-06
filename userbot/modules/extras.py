import asyncio, subprocess
from userbot import bot, LOGGER, LOGGER_GROUP
from telethon import events
from telethon.events import StopPropagation
from telethon.tl.functions.messages import ExportChatInviteRequest
from telethon.tl.functions.contacts import BlockRequest
from telethon.tl.functions.channels import LeaveChannelRequest, CreateChannelRequest, DeleteMessagesRequest
from lmgtfy import lmgtfy

@bot.on(events.NewMessage(outgoing=True, pattern='^\.timer '))
@bot.on(events.MessageEdited(outgoing=True, pattern='^\.timer '))
async def timer_blankx(e):
	txt=e.text[7:] + '\nDeleting in '
	j=10
	k=j
	for j in range(j):
		await e.edit(txt + str(k))
		k=k-1
		await asyncio.sleep(1)
	await e.delete()

@bot.on(events.NewMessage(outgoing=True, pattern='^\.stimer '))
@bot.on(events.MessageEdited(outgoing=True, pattern='^\.stimer '))
async def stimer_blankx(e):
	await e.edit(e.text[7:])
	await asyncio.sleep(10)
	await e.delete()

@bot.on(events.NewMessage(outgoing=True, pattern='^\.time$'))
@bot.on(events.MessageEdited(outgoing=True, pattern='^\.time$'))
async def time_blankx(e):
	if e.reply_to_msg_id != None:
		thed='Deleting replied to message in '
		j=10
		k=j
		for j in range(j):
			await e.edit(thed + str(k))
			k=k-1
			await asyncio.sleep(1)
		await bot.delete_messages(e.input_chat, [e.reply_to_msg_id, e.id])

@bot.on(events.NewMessage(outgoing=True, pattern='^\.stime$'))
@bot.on(events.MessageEdited(outgoing=True, pattern='^\.stime$'))
async def stime_blankx(e):
	await e.delete()
	if e.reply_to_msg_id != None:
		await asyncio.sleep(10)
		await bot.delete_messages(e.input_chat, [e.reply_to_msg_id])

@bot.on(events.NewMessage(outgoing=True, pattern='^\.sedit '))
@bot.on(events.MessageEdited(outgoing=True, pattern='^\.sedit '))
async def sedit_blankx(e):
	await e.edit('s/\X+/' + e.text[7:])
	await e.delete()

@bot.on(events.NewMessage(outgoing=True, pattern='^\.sedita '))
@bot.on(events.MessageEdited(outgoing=True, pattern='^\.sedita '))
async def sedit_blankx(e):
	await e.delete()
	if e.reply_to_msg_id != None:
		f=await bot.send_message(await bot.get_input_entity(e.chat_id), message='s/((.+|\\n+))+/' + e.text[8:], reply_to=e.reply_to_msg_id)
		await asyncio.sleep(0.25)
		await f.delete()

@bot.on(events.NewMessage(outgoing=True, pattern="^.block$"))
@bot.on(events.MessageEdited(outgoing=True, pattern="^.block$"))
async def blocks(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        if '-' not in str(e.chat_id):
            await bot(BlockRequest(await bot.get_input_entity(e.chat_id)))
        else:
            await e.edit('`In PM sar`')

@bot.on(events.NewMessage(outgoing=True, pattern="^.leave$"))
@bot.on(events.MessageEdited(outgoing=True, pattern="^.leave$"))
async def leave(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        if '-' in str(e.chat_id):
            await bot(LeaveChannelRequest(e.chat_id))
        else:
            await e.edit('`Sar This is Not A Chat`')

@bot.on(events.NewMessage(outgoing=True, pattern="^.speedtest$"))
@bot.on(events.MessageEdited(outgoing=True, pattern="^.speedtest$"))
async def speedtest(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        l = await e.reply("`Running Speedtest Simple...`")
        k=subprocess.run(['speedtest', '--simple'], stdout=subprocess.PIPE)
        await l.edit("`" + k.stdout.decode()[:-1] + "`")

@bot.on(events.NewMessage(pattern='^\.figlet (.+)'))
@bot.on(events.MessageEdited(pattern='^\.figlet (.+)'))
async def figlety(e):
	l=['figlet']
	l+=e.pattern_match.group(1).split(' ')
	p='```'
	p+=subprocess.run(l, stdout=subprocess.PIPE).stdout.decode()
	p+='```'
	await e.edit(p)

@bot.on(events.NewMessage(pattern='^\.toilet (.+)'))
@bot.on(events.MessageEdited(pattern='^\.toilet (.+)'))
async def toilett(e):
        l=['toilet']
        l+=e.pattern_match.group(1).split(' ')
        p='```'
        p+=subprocess.run(l, stdout=subprocess.PIPE).stdout.decode()
        p+='```'
        await e.edit(p)

@bot.on(events.NewMessage(pattern='^\.cs (.+)'))
@bot.on(events.MessageEdited(pattern='^\.cs (.+)'))
async def cowsay(e):
        l=['cowsay']
        l+=e.pattern_match.group(1).split(' ')
        p='```'
        p+=subprocess.run(l, stdout=subprocess.PIPE).stdout.decode()
        p+='```'
        await e.edit(p)  

@bot.on(events.NewMessage(pattern="^.lmg", outgoing=True))
@bot.on(events.MessageEdited(pattern="^.lmg", outgoing=True))
async def let_me_google_that_for_you(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        textx = await e.get_reply_message()
        message = e.text
        if message[8:]:
            message = str(message[8:])
        elif textx:
            message = str(textx.message)
        reply_text = 'http://lmgtfy.com/?s=g&iie=1&q=' + message.replace(" ", "+")
        await e.edit(reply_text)
        if LOGGER:
            await bot.send_message(
                LOGGER_GROUP,
                "LMGTFY query " + message + " was executed successfully",
            )     
