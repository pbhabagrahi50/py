test="python is awesome"
hello=test.upper()
hrllo1=hello.replace("awesome","best")
print('really:',hrllo1)
word= hrllo1.split()
print("split word :",word)
substring= "is"
substring1="AWESOME"
if substring in test:   
  print("sub-string found:",substring)
  import re
  fix=input("Please put key = ")
  print(fix)
  found=re.search(fix,test)
  if found :
     print("sub-string found:",found.group())
  else:
     print("pattern not found")
