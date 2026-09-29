def power (p, n):
   if n == 0:
      return 1
   else:
     return p * power (p, n - 1)
p = float (input ("Enter principal/base value: "))
n = int (input ("Enter number of years/powers: "))
result = power (p, n)
print("Power =", result)
