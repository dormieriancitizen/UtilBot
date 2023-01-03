import os, time

import discord

from colorama import init
from colorama import Fore, Style

init()

import settings.settings as set
import commands as cme


class bot(discord.Client):
  def __init__(self):
    
    self.auth = []
    self.blockedservers = []
    
    print("Loading Verified Users")
    with open('./settings/authusers.txt', 'r') as authlist:
      for user in authlist.readlines():
        self.auth.append(int(user))
        
    print("Loading Blocked Servers")
    with open('./settings/blockedservers.txt', 'r') as serverlist:
      for user in serverlist.readlines():
        self.blockedservers.append(int(user))    

    print("Initializing...")
    super().__init__()
    
  async def on_ready(self):
    print(f"{Fore.GREEN} TOKEN SUCESS {Style.RESET_ALL}")
    time.sleep(0.1)
    os.system('clear')
    print(
      f'Logged on as{Style.RESET_ALL}{Fore.RED} {self.user} {Style.RESET_ALL}')

  async def on_message(self, message):
    # print(message.guild.id)
    # print(self.blockedservers)
    # print(message.guild.id in self.blockedservers)
    
    if message.guild.id in self.blockedservers:
      return
    
    for item in set.responses:
      if item in message.content.lower():
        await message.reply(set.responses[item])
        print(f"{Style.DIM} sent {Style.RESET_ALL}{Fore.GREEN}{set.responses[item]}{Style.RESET_ALL}")
  
    if message.content.startswith(set.prefix):
      self.ver = message.author.id in self.auth or message.author == self.user
      print(
        f"{Style.DIM} recieved command {Style.RESET_ALL}{Fore.BLUE}{message.content} from {Fore.MAGENTA}{message.author}{Style.RESET_ALL} ({f'{Fore.BLUE}SelfUser' if self.ver else f'{Fore.RED}OtherUser'}{Style.RESET_ALL})"
      )

      m = message.content.split(set.prefix)[1]
      m = m.split(' ')
      cmd = m.pop(0)
      args = m

      try:
        response = await cme.commandlist[cmd](args, message, self)
      except KeyError:
        response = f"HaychBot doesn't know what `{cmd}` is"
      except Exception as error:
        response = f"There was an error: ```{error}```"

      if response != False:
        await message.reply(str(response))
        print(
          f"{Style.DIM} sent {Style.RESET_ALL}{Fore.GREEN}{response}{Style.RESET_ALL}"
      )
    else:
      return


client = bot()
