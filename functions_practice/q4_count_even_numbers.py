def func(*x):
    if not x:
        return "No Values Passed"
    num = 0
    for i in x:
      if i%2 == 0:
       num += 1
    return num
a = func(4,6,5,8,34,56,47,65,89,70)
print(a)

