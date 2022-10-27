import time
import cmd.nuke, cmd.spam, cmd.dofancymath

async def echo(args,message,self):
  if not self.ver:
      answer = f"{message.author.mention} ran a command and {self.user.mention} bears no responsiblity \n {' '.join(args)}"
  else:
      answer = ' '.join(args)
  return(answer)
  

async def ping(args,message,self):
  return("pong")


async def thread(args,message,self):
  if self.ver:
    messages = await message.channel.history(limit=int(args[0])+1).flatten()
    messages.pop(0)
    for toThread in messages:
      await toThread.channel.create_thread(name="Thread", minutes=60, message=toThread)
    return f"last {args[0]} messages threaded"

async def execute(args,message,self):
  if self.ver:
    exec(" ".join(args))
    return "Guillotined"
  else:
    return "haha no arbitary code execution is very dangerous"

commandlist = {
  "echo":echo,
  "ping":ping,
  "math":cmd.dofancymath.domath,
  "nuke":cmd.nuke.nuke,
  "thread":thread,
  "exec":execute,
  "spam":cmd.spam.spam,
}