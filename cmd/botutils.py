import os, socket
from colorama import Style, Fore, init
init()

async def execute(args,message,self):
  if self.ver:
    exec(" ".join(args))
    return "Guillotined"
  else:
    return "haha no arbitary code execution is very dangerous"

async def ping(args,message,self):
  return "pong"

async def clear(args,message,self):
  os.system("clear")
  print(f'Logged on as{Style.RESET_ALL}{Fore.RED} {self.user} {Style.RESET_ALL}')
  return False

async def source(args,message,self):
  return "https://replit.com/@firedestroyer/UtilBot"

async def rundetails(args,message,self):
  if not self.ver:
    return "No"

  details = {
    "Hostname":socket.gethostname(),
    "IP Address":socket.gethostbyname(socket.gethostname()),
    "Uptime":os.popen('uptime').read().rstrip(),
  }

  toReturn = ""
  
  for i in details:
    toReturn += i+":"+details[i]+"\n"

  return "```"+toReturn+"```"