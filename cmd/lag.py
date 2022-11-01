import time

async def lag(args,message,self):
  if not self.ver:
    return "nu"
  amount = args.pop(0)
  msg = "🅰"*1990
  await message.channel.send("And thus, it ends.")
  for i in range(int(amount)):
    time.sleep(0.05)
    await message.channel.send(msg)
  return('Pain? Unless your on a phone then not.')