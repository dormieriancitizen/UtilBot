import random
from colorama import Style, Fore, init
init()

async def rockpaperscissors(args,message,self):
  options = [
    "rock",
    "paper",
    "scissors"
  ]
  
  return options[random.randrange(0,2)]