import os, time

import discord

import settings.settings as set
import settings.style as style
import commands as cme


class bot(discord.Client):

  def __init__(self):
    self.auth = []
    self.blockedservers = []
    self.uptime = time.time()

    print("Loading Verified Users")
    with open('./settings/authusers.txt', 'r') as authlist:
      for user in authlist.readlines():
        self.auth.append(int(user))

    print("Loading Blocked Servers")
    with open('./settings/blockedservers.txt', 'r') as serverlist:
      for user in serverlist.readlines():
        self.blockedservers.append(int(user))

    print("Loaded")
    time.sleep(0.01)
    os.system('clear')
    
    print("Logging on...")
    super().__init__()

  async def on_ready(self):
    print(f"{style.Fore.GREEN} TOKEN SUCESS")
    time.sleep(0.1)
    os.system('clear')
    print(f'{style.style.RESET_ALL} Logged on as{style.user} {self.user}')

  async def on_message(self, message):
    # print(message.guild.id)
    # print(self.blockedservers)
    # print(message.guild.id in self.blockedservers)

    if message.guild.id in self.blockedservers:
      return

    for item in set.responses:
      if item in message.content.lower():
        await message.reply(set.responses[item])
        print(f"{style.log} sent {style.sent}{set.responses[item]}")

    if message.content.startswith(set.prefix):
      self.ver = message.author.id in self.auth or message.author == self.user

      print(
        f"{style.log} recieved command {style.command}{message.content} from {style.user}{message.author}"
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
        print(f"{style.log} sent {style.sent}{response}")
    else:
      return


client = bot()
