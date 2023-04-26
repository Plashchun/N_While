n = int(input('enter from number: '))
i = 0
while i < n:
   i += 3
   print(i)



n = int(input('enter from number: '))
i = 0
k = i
summ = 0
while i <= n:
    if not k and i % 2 != 0:
      summ += i
    i += 1

print(f'Sum of numbers {n}: {summ}')