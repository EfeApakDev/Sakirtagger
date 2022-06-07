import os, logging, asyncio
import random
from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)

api_id = int(os.environ.get("APP_ID"))
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("TOKEN")
client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)

anlik_calisan = []

# Əkmə Oğlum...!!!
emj = ['😇','🥰','😎','🤩','😍','👾','🤡','🥳','😻','😼','😽','💋','👸','🤴','🎅🏻','🤶','🧞‍♀️','🧞','🧞‍♂️','🧜‍♀️','🧜','🧚‍♀️','🧚','👑','💍','🕶','🐶','🐱','🐭','🐹','🐰','🦊','🐻','🐼','🐨','🐯','🦁','🐮','🐷','🐽','🐸','🐵','🙈','🙉','🙊','🐒','🐣','🐥','🦅','🐝','🦋','🐞','💐','🌹','🥀','🌺','🌸','🌼','🌻','⭐️','🌟','✨','⚡️','🔥','🌈','☃️','🍫','💅','🐺','🍫','🍕','☕','🧸','🦅','👩‍🦰','🎮','☄️','🌙','🦕','👨🏻‍✈️','🥶','🍿','👀','💀','💟','♥️','💘','💝','💗','💙','💛','🖤','🤑','⚡','😈','🤡','🎊','🔥','😼','💤','✊','👩‍🎨','🧕','🌼','💐','🌹','🥀','🌷','🌺','🌸','🏵️','🌻','🍂','🍁','🌾','🌱','🌿','🍃','☘️','🍀','🌵','🌴','🌳','🌲','🏞️','🌪️','☃️','⛄','❄️','🏔️','🌋','🙋','🤶','👩‍💼','🧓','🧔','💃','🕺','👩‍🦰','🪐','🦄','🐢','🐁','🐤','🐣','🐥','🦉','🐓','🕊️','🦢','🦩','🦈','🐬','🐋','🐳','🐟','🐠','🦚','🐡','🦐','🦞','🦀','🦑','🐙','🦂','🕷️','🕸️','🐜','🦗','🦟','🐝','🐞','🐾','🍓','🍒','🍎','🍉','🍊','🥭','🍍','🍋','🍇','🥝','🍐','🥥','🌶️','🍄','🍔','🧆','🥙','🦞','🍧','🍨','🍦','🥧','🍰','🍮','🎂','🧁','🍭','🍬','🍩','🍺','🍻','🥂','🍾','🍷']
# Əkmə Oğlum...!!!

#  güzel isimler...!!! 
cumle = ['Üzümlü kekim ✨', 'Nar çiçeği ✨', 'Papatya 🌼', 'Karanfil ✨', 'Gül 🌹', 'Ayıcık 🐻', 'Mutlu pandam 🐼', 'Ay parem ✨', 'Ballı lokmam ✨', 'Bebişim 🥰', 'Lale 🌷', 'Zambak ⚜', 'Nergis ✨', 'Sümbül ☘️', 'Nilüfer ☘️', 'Menekşe ⚜️', 'Lavanta ✨', 'Gül pare ✨', 'Reyhan 🌷', 'Kaktüs ⚜️', 'Böğürtlen ☘️', 'Orkide ☘️', 'Manolya ✨', 'Ayçiçeği ✨', 'Tweety ⚜️', 'Star ✨', 'Yonca 🍀', 'Ateş böceği ✨',]
#  güzel isimler...!!!

@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)


@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  await event.reply("**Bozkurt Tagger Bot 🇹🇷**, Grup veya kanaldaki neredeyse tüm üyelerden bahsedebilirim ★\nDaha fazla bilgi için **/bilgi**'i tıklayın.",
                    buttons=(
                      [
                         Button.url('➕ BENİ GRUBA EKLE ➕ ', 'http://t.me/bozkurtaggerbot?startgroup=a')
                      ],
                      [
                         Button.url('📣 Kanal', 'https://t.me/bozkurtRoBot'),
                         Button.url('👮Sahip', 'https://t.me/bozkurt20'),
                         Button.url('🎆 Support', 'https://t.me/muhabbetofkings')
                      ]
                    ),
                    link_preview=False
                   )
@client.on(events.NewMessage(pattern="^/bilgi$"))
async def help(event):
  helptext = "**Bozkurt Tagger Bot 🇹🇷 Bot'un Yardım Menüsü**\n\nKomut: /utag \n  Bu komutu, başkalarına bahsetmek istediğiniz metinle birlikte kullanabilirsiniz. /etag  \n emoji ile etiketleme. \n`Örnek: /utag Günaydın!`  \nBu komutu yanıt olarak kullanabilirsiniz. herhangi bir mesaj Bot, yanıtlanan iletiye kullanıcıları etiketleyecek."
  await event.reply(helptext,
                    buttons=(
                      [
                         Button.url('➕ BENİ GRUBA EKLE ➕', 'http://t.me/bozkurtaggerbot?startgroup=a')
                      ],
                      [
                          Button.url('📣 Kanal', 'https://t.me/bozkurtRoBot'),
                         Button.url('👮Sahip', 'https://t.me/bozkurt20'),
                         Button.url('🎆 Support', 'https://t.me/muhabbetofkings')
                      ]
                    ),
                    link_preview=False
                   )


@client.on(events.NewMessage(pattern="^/utag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("__Bu komut gruplarda ve kanallarda kullanılabilir.!__")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("__Yalnızca yöneticiler hepsinden bahsedebilir!__")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("__Eski mesajlar için üyelerden bahsedemem! (gruba eklemeden önce gönderilen mesajlar)__")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("__Bana bir argüman ver!__")
  else:
    return await event.respond("__Bir mesajı yanıtlayın veya başkalarından bahsetmem için bana bir metin verin!__")
    
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"👤 - [{usr.first_name}](tg://user?id={usr.id}) \n"
      if event.chat_id not in anlik_calisan:
        await event.respond("İşlem Başarılı Bir Şekilde Durduruldu ❌")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"👤 - [{usr.first_name}](tg://user?id={usr.id}) \n"
      if event.chat_id not in anlik_calisan:
        await event.respond("İşlem Başarılı Bir Şekilde Durduruldu ❌")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

# Emoji Modulu (aykhan_s)
@client.on(events.NewMessage(pattern="^/itag ?(.*)"))
async def etag(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("__Bu komut gruplarda ve kanallarda kullanılabilir.!__")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("__Yalnızca yöneticiler hepsinden bahsedebilir!__")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("__Eski mesajlar için üyelerden bahsedemem! (gruba eklemeden önce gönderilen mesajlar)__")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("__Bana bir argüman ver!__")
  else:
    return await event.respond("__Bir mesajı yanıtlayın veya başkalarından bahsetmem için bana bir metin verin!__")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(cumle)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("İşlem Başarılı Bir Şekilde Durduruldu ❌")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(cumle)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("İşlem Başarılı Bir Şekilde Durduruldu ❌")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

#  güzel isimler...!!!
@client.on(events.NewMessage(pattern="^/etag ?(.*)"))
async def nick(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("__Bu komut gruplarda ve kanallarda kullanılabilir.!__")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("__Yalnızca yöneticiler hepsinden bahsedebilir!__")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("__Eski mesajlar için üyelerden bahsedemem! (gruba eklemeden önce gönderilen mesajlar)__")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("__Bana bir argüman ver!__")
  else:
    return await event.respond("__Bir mesajı yanıtlayın veya başkalarından bahsetmem için bana bir metin verin!__")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(emj)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("İşlem Başarılı Bir Şekilde Durduruldu ❌")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(emj)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("İşlem Başarılı Bir Şekilde Durduruldu ❌")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

@client.on(events.NewMessage(pattern="^/tektag ?(.*)"))
async def mentionall(event):
  global tekli_calisan
  if event.is_private:
    return await event.respond("**Bu komutu gruplar ve kanallar için geçerli❗️**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu komutu sadace yoneticiler kullana bilir〽**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**önceki mesajı etiketleye bilmerim*")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("Başlamak için Sebep Yazın❗️")
  else:
    return await event.respond("**Işleme başlamağım için sebeb yazın..**")
  
  if mode == "text_on_cmd":
    tekli_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"**[{usr.first_name}](tg://user?id={usr.id})**"
      if event.chat_id not in tekli_calisan:
        await event.respond("**Işlem Başarıyla Durduruldu\n\n**Buda sizin reklamınız ola bilir @bozkurtaggerbot**❌****")
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, f"{usrtxt} {msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    tekli_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id})"
      if event.chat_id not in tekli_calisan:
        await event.respond("Işlem Başarıyla Durduruldu\n\n**Buda sizin reklamınız ola bilir @bozkurtaggerbot**❌**")
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

print(">> Bot çalışıyor <<")
client.run_until_disconnected()