import os, time
os.system("pip uninstall discord")
os.system("pip uninstall discord-py")
import discord

from colorama import init
from colorama import Fore, Style
init()

import settings.settings as set
import commands as cme  

class bot(discord.Client):
  async def on_ready(self):
    print(f"{Fore.GREEN} TOKEN SUCESS {Style.RESET_ALL}")
    time.sleep(0.1)
    os.system('clear')
    self.auth = []

    with open('./settings/authusers.txt','r') as authlist:
      for user in authlist.readlines():
        self.auth.append(await client.fetch_user(user))
    
    
    print(f'Logged on as{Style.RESET_ALL}{Fore.RED} {self.user} {Style.RESET_ALL}')

  async def on_message(self, message):
    if message.content.startswith(set.prefix):
      self.ver = message.author in self.auth
      print(f"{Style.DIM} recieved command {Style.RESET_ALL}{Fore.BLUE}{message.content} from {Fore.MAGENTA}{message.author}{Style.RESET_ALL} ({f'{Fore.BLUE}SelfUser' if self.ver else f'{Fore.RED}OtherUser'}{Style.RESET_ALL})")
      
      
      m = message.content.split(set.prefix)[1]
      m = m.split(' ')
      cmd = m.pop(0)
      args = m

      try:
        response = await cme.commandlist[cmd](args,message,self)
      except KeyError:
        response = f"HaychBot doesn't know what `{cmd}` is"
      except Exception as error:
        response = f"There was an error: ```{error}```"
      await message.reply(response)

      print(f"{Style.DIM} sent {Style.RESET_ALL}{Fore.GREEN}{response}{Style.RESET_ALL}")
    else:
      return

client = bot()
