import server, os

from colorama import init
from colorama import Fore, Style
init()

import discord
try:
  if discord.__version__ != "1.9.2":
    print("INVALID DISCORD VERSION, UNINSTALLING NONSENSE")
    os.system("pip uninstall discord -y")
    os.system("pip uninstall discord-py -y")
    quit()
  else:
    print("CORRECT DISCORD VERSION")
    
except AttributeError:
  print("BORKED DISCORD VERSION, FIXING")
  os.system("pip uninstall discord -y")
  os.system("pip uninstall discord-py -y")
  os.system("pip uninstall discord.py-self -y")
  os.system("pip install discord.py-self")
  quit()
  

import clientmanager

def logOn():
  try:
    try:
      token = os.environ["token"]
    except:
      token = input("token?: ")

    print(f"{Fore.BLUE}CHECKING TOKEN {Style.RESET_ALL}")
    clientmanager.client.run(token)
  except clientmanager.discord.errors.LoginFailure:
    print(f"{Fore.RED}INVALID TOKEN.{Style.RESET_ALL} \n \n \n")
    
try:
    logOn()
except Exception as Error:
    print(Style.RESET_ALL+"Something went wrong: \n"+Fore.RED+str(Error))
    server.kool.join()
    os.system("kill 1")

print("Something went very wrong.")