import time
from colorama import init, Fore, Style
init()

async def nuke(args,message,self):
  if self.ver:
    messages = await message.channel.history(limit=int(args[0])+1).flatten()
    messages.pop(0)
    for toDel in messages:
      try:
        time.sleep(0.1)
        await toDel.delete()
      except:
        print(f"{Fore.RED} Attempted to permlesss nuke {Style.RESET_ALL}")
    return f"last {args[0]} messages deleted"
  else:
    return("delete it urself bozo")