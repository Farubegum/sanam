sam=int(input())
san=list(map(int,str(sam)))
kad=list(map(lambda x:x**3,san))
if(sum(kad)==sam):
  print("yes")
else:
  print("no")
