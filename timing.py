import time, math

t1 = time.time()

for i in range(50):
    x = math.factorial(i)
    print(f' at {i}: fact {x}')

print(f' time to run test was {(time.time() - t1)}')