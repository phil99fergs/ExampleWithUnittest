def fibionacci(n):
    old, new = 0, 1
    for _ in range(n):
        old, new = new, old + new
    return old


# Rekursīva Fibonacci skaitļa aprēķināšanas funkcija
def rfibionacci(n):
    if n < 0:
      print("Nepareizs ievads, nevar būt mazāk par 0")
    elif n == 0:
      return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return rfibionacci(n-1) + rfibionacci(n-2)
       


fibionacci(5)
rfibionacci(3)