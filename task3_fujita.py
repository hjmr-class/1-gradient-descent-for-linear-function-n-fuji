import random

alpha = 0.001
a, b, c = 0, 0, 0

def func_y_hat(x):
  y_hat = 3.0 * x**2 + 5.0 * x - 3.0
  return y_hat

def func_y(x):
  y = a * x**2 + b * x + c
  return y

def func_error(y, y_hat):
  e = 0.5 * (y - y_hat) **2
  return e

def func_da(x):
  y = func_y(x)
  y_hat = func_y_hat(x)
  da = (y - y_hat) * x**2
  return da

def func_db(x):
  y = func_y(x)
  y_hat = func_y_hat(x)
  db = (y - y_hat) * x
  return db

def func_dc(x):
  y = func_y(x)
  y_hat = func_y_hat(x)
  dc = (y - y_hat) * 1
  return dc

def init_parameters():
  a = random.random()
  b = random.random()
  c = random.random()
  return a, b, c

i, j = 0, 0
init_parameters()

for i in range(500):
  e_sum = 0
  for j in range(100):
    x = random.random() * 10 - 5
    a -= alpha * func_da(x)
    b -= alpha * func_db(x)
    c -= alpha * func_dc(x) 
    e_sum += func_error(func_y(x), func_y_hat(x))

  e_ave = e_sum / 100
  print(str(i) + ", " + str(e_ave))
print("a = " + str(a) + ", b = " + str(b) + ", c = " + str(c))