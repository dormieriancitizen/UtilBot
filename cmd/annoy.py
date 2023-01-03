import time
from colorama import init, Fore, Style
init()



async def lag(args,message,self):
  if not self.ver:
    return "nu"
  amount = args.pop(0)
  msg = "🅰"*1990
  await message.channel.send("haha L")
  for i in range(int(amount)):
    time.sleep(0.05)
    await message.channel.send(msg)
  return "Dun"

async def spam(args,message,self):
  if not self.ver:
    return "haha no all the power is for myself"
  amount = args.pop(0)
  msg = " ".join(args)
  for i in range(int(amount)):
    time.sleep(0.05)
    await message.channel.send(msg)
  return False

async def spoil(args,message,self):
  if not self.ver:
    return False
  msg = " ".join(args)
  await message.delete()
  sender = list(msg)
  await message.channel.send('||'+"||||".join(sender)+"||")

async def ghostping(args,message,self):
  await message.delete()
  return False
