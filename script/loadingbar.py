import time
start = time.perf_counter() # 时间开始
step = 100 # 步骤（加载次数）
bar = 20 # 进度条尺寸
print(r"{0:-^20}".format("开始执行")) # 显示“开始执行”，在20个“-”之中
for n in range(step): # 按照step（步骤）循环
  now = time.perf_counter() - start # 现在执行时间
  per = (n/(step - 1)) # 百分比
  process = int(per * bar) # 进程
  star = "*" * process # 按照进程输出“*”
  dot = "." * (bar - process) # 未读取的输出“.”
  print("\r{:^6.2f}%[{}->{}]{:.2f}s".format(per* 100, star, dot, now), end='') # 输出
  time.sleep(0.1) # 间隔0.1秒
print("\n"+"{0:-^20}".format("执行结束")) # 显示“执行结束”，在20个“-”之中