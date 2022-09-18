import random
from num2words import num2words

small = random.randint(0, 99)
good = random.randint(0, 9999)
big = random.randint(99, 999999999)
real = random.randint(0, 9999) + round(random.random(), 2)

print(small, num2words(small))
print(good, num2words(good) if num2words(good, to='cardinal') == num2words(good, to='year') else
      f"{good}, {num2words(good, to='year')} ({num2words(good)})")
print(big, num2words(big))
print(real, num2words(real))

