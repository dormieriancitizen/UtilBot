import time

async def spam(args,message,self):
  if not self.ver:
    return "haha no all the power is for myself"
  amount = args.pop(0)
  msg = " ".join(args)
  for i in range(int(amount)):
    time.sleep(0.05)
    await message.channel.send(msg)
  return('spam complete')