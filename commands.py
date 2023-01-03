import cmd as c

async def getslash(args,message,self):
  commands = [command async for command in message.channel.slash_commands()]
  return commands
    
async def facepalm(args,message,self):
  await message.channel.send("(－‸ლ)")
  await message.delete()
  return False

commandlist = {
  "echo":c.utils.echo,
  "ping":c.botutils.ping,
  "exec":c.botutils.execute,
  "clear":c.botutils.clear,
  "nuke":c.utils.nuke,
  "spam":c.annoy.spam,
  "lag":c.annoy.lag,
  "getslash":getslash,
  "facepalm":facepalm,
  "spoil":c.annoy.spoil,
  "source":c.botutils.source,
  "ghostping":c.annoy.ghostping,
  "rockpaperscissors":c.fun.rockpaperscissors,
  "rundetails":c.botutils.rundetails,
}
