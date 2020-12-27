# pi_archimedes.py
'''
The program outputs a value of pi for a given number of a decimal places according to Archimedes algorithm.
The maximum precision is limited to 15 decimal places.
The program will do the iterations (increasing the polygon side number) until the digit on given number + 1 stabilize.
While loop is implemented to ensure the integer number is entered  

'''

while True:
    try:
        num = int(input('Enter the number of pi decimals (maximum 15 decimal digits): '))
        break
    except:
        continue

n = 6
s = 1.0
pi_contr = 1.0

while True:

    a = (1-(s/2)**2)**0.5
    b = 1 - a
    circumference = n*s
    pi_arch = circumference/2

    s_new = (b**2 + (s/2)**2)**0.5
    s = s_new
    n *= 2

    if round(pi_arch, num+1) == round(pi_contr, num+1):
        break
        
    pi_contr = pi_arch

print(round(pi_arch, num))