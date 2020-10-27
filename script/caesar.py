orgin = input() # 输入原始值
passwd = "" # 加密之后的内容
primeUpper = ord("A") # 字母“A”的ascii值
primeLower = ord("a") # 字母“a”的ascii值
for latter in orgin: # 循环输入原始值
  if "z" >= latter >= "a": # 小写字母
    passwd += chr(primeLower + (ord(latter) - primeLower + 3)%26) # 小写字母加密，字母向后3位比如a会变成d，y会变成b
  elif "Z" >= latter >= "A": # 大写字母
    passwd += chr(primeUpper + (ord(latter) - primeUpper + 3)%26) # 大写字母加密
  else: # 不是字母不加密
    passwd += latter # 字段重新排列为加密之后的值
print(passwd) # 打印密码