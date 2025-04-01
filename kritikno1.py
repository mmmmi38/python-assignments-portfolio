x=float(input(print("enter number between 0 and 1")))
#takes + sets our input to a float for calculations
if 0<=x<=1:
    def error(a,b):
        y = (a**(2*b+1))/(2*b+1)
        return y
    n = 0
    while error(x,n) > 0.0001:
        n += 1
    sum = 0
    for i in range (n):
        sum = sum + (((-1)**i) * x**(2*i + 1)) / (2*i + 1)
    print(sum, n, error (x, n))
else:
    print("error")


