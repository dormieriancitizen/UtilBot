import server, os, clientmanager

from colorama import init
from colorama import Fore, Style
init()

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
except:
    server.kool.join()
    os.system("kill 1")