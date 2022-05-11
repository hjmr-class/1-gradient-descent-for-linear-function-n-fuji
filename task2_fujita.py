import random

alpha = 0.001
a = 0
b = 0

def func_y_hat(x):
  y_hat = 5.0 * x - 3.0 + random.random()
  return y_hat

def func_y(x):
  y = a * x + b
  return y

def func_error(y, y_hat):
  e = 0.5 * (y - y_hat) * (y - y_hat)
  return e

def func_da(x):
  y = func_y(x)
  y_hat = func_y_hat(x)
  da = (y - y_hat) * x
  return da

def func_db(x):
  y = func_y(x)
  y_hat = func_y_hat(x)
  db = (y - y_hat) * 1
  return db

def rand_one():
  r = random.random()
  return r

def init_parameters():
  a = rand_one()
  b = rand_one()
  return a, b

i, j = 0, 0
init_parameters()

for i in range(500):
  e_sum = 0
  for j in range(100):
    x = rand_one() * 100 - 50
    a -= alpha * func_da(x)
    b -= alpha * func_db(x)
    e_sum += func_error(func_y(x), func_y_hat(x))

  e_ave = e_sum / 100
  print(str(i) + ", " + str(e_ave))
print("a = " + str(a) + ", b = " + str(b))