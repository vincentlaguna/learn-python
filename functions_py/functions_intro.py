# Multiple return values on functions:

def get_boundaries(target, margin):
  low_limit = target - margin
  high_limit = margin + target
  return low_limit, high_limit

low, high = get_boundaries(100, 20)

print("target has a low limit of " + str(low) + 
" and margin has a high limit of " + str(high))

# Basic physics project using functions:

train_mass = 22680
train_acceleration = 10
train_distance = 100

bomb_mass = 1

def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp

f100_in_celsius = f_to_c(100)

def c_to_f(c_temp):
  f_temp = (c_temp * 9/5) + 32
  return f_temp

c0_in_farenheit = c_to_f(0)

def get_force(mass, acceleration):
  return mass * acceleration

train_force = get_force(train_mass, train_acceleration)

print("The GE train supplies " + str(train_force) + " Newtons of force.")

c = 3*10**8

def get_energy(mass, c):
  return mass * c

bomb_energy = get_energy(bomb_mass, c)

print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.")

def get_work(mass, acceleration, distance):
  force = get_force(mass, acceleration) * distance
  return force

train_work = get_work(train_mass, train_acceleration, train_distance)

print("The GE train does " + str(train_work) + " Joules of work over " + 
str(train_distance) + " meters.")