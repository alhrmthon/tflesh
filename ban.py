import asyncio
from pyrogram import Client,filters,enums

api_id = int(os.environ.get("APP_ID"))
api_hash = os.environ.get("API_HASH")
sessionstring = os.environ.get("sessionstring")
app = Client("acc", session_string = sessionstring, api_id = api_id, api_hash = api_hash)

@app.on_message(filters.command("حظر الكل","") & filters.me)
async def num(client, message):
  i = 1
  xx = 0
  async for x in app.get_chat_members(message.chat.id):
    try :
      await app.ban_chat_member(message.chat.id,x.user.id)
      if i%10 == 0 :
          await message.edit(f"• تم حظر {i}")
      i += 1
    except :
      xx +=1
      await message.edit(f"• العضو {x.user.id} لم استطيع حظره")
  await message.edit(f"• تم حظر {i} عضو \n• لم استطيع حظر {xx} عضو")

@app.on_message(filters.command("مسح المحظورين","")& filters.me)
async def bn(client ,message):
  xxx = 0
  await message.edit("• جاري الغاء الحظر ...")
  async for m in app.get_chat_members(message.chat.id, filter=enums.ChatMembersFilter.BANNED):
    try :
      await app.unban_chat_member(message.chat.id , m.user.id)
      xxx += 1
    except :
      print("error")
  await message.edit(f"تم الغاء حظر {xxx} عضو")


app.run()