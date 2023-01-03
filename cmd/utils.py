import time, asyncio
from colorama import init, Fore, Style
init()

async def echo(args,message,self):
  if not self.ver:
      answer = f"{message.author.mention} ran a command and {self.user.mention} bears no responsiblity \n {' '.join(args)}"
  else:
      answer = ' '.join(args)
  return(answer)

async def nuke(args,message,self):
  if self.ver:
    messages = await message.channel.history(limit=int(args[0])+1).flatten()
    messages.pop(0)
    for toDel in messages:
      try:
        await asyncio.sleep(0.3)
        await toDel.delete()
      except:
        print(f"{Fore.RED} Attempted to permlesss nuke {Style.RESET_ALL}")
    return f"last {args[0]} messages deleted"
  else:
    return("delete it urself bozo")

