async def domath(args,message,self):
  equation = ' '.join(args)
  if '+' in equation:
    y = equation.split('+')
    x = int(y[0])+int(y[1])
  elif '-' in equation:
    y = equation.split('-')
    x = int(y[0])-int(y[1])
  elif '/' in equation:
    y = equation.split('-')
    x = int(y[0])/int(y[1])
  elif '*' in equation:
    y = equation.split('-')
    x = int(y[0])*int(y[1])
  return f"{equation} = {x}"