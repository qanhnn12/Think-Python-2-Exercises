import math

# Question 1
r = 5
volume = 4 / 3 * math.pi * r ** 3
print('Q1: The volume of a sphere with radius 5 is', volume)

# Question 2
price = 24.95
after_discount_price = 0.6 * price
first_copy = 3
next_copy = 0.75

shipping_cost = first_copy + next_copy * 59
total_cost = after_discount_price * 60 + shipping_cost
print('Q2: The total wholesale cost for 60 coppies is', total_cost)

# Question 3
start = (6 * 60 + 52) * 60
easy = (8 * 60 + 15) * 2
tempo = (7 * 60 + 12) * 3

hour = (start + easy + tempo) / 3600
hour_int = int(hour)
minute = (hour - hour_int) * 60
minute_int = int(minute)

print(f"Q3: Breakfast time is at {hour_int}:{minute_int}")
