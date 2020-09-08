# break terminates loop completely
for val in [10, 20, 30, 45, 50]:
    if val == 45:
        break
    print(f' val is {val}')

print(f'\n')

# continue terminates current iteration and proceeds to next iteration
for val in [10, 20, 30, 45, 50]:
    if val == 45:
        continue
    print(f' val is {val}')
