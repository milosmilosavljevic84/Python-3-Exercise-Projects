# pi_archimedes.py

# The program outputs a value of pi for a given number of a decimal places according to Archimedes algorithm.
# The maximum precision is limited to 15 decimal places.
# The program will do the iterations (increasing the polygon side number) until the digit on given number + 1 stabilize.
# While loop is implemented to ensure the integer number is entered  
# In case the negative number od decimal places is entered the value of 0.0 is returned 


while True:
    try:
        num = int(input('Enter the number of pi decimals (maximum 15 decimal digits): '))
        break
    except:
        continue

num_of_sides = 6
length_of_side = 1.0
pi_previous = 1.0

while True:

    triangle_height = (1-(length_of_side/2)**2)**0.5
    circumference = num_of_sides * length_of_side
    pi_archimedes = circumference/2

    length_of_side = ((1 - triangle_height)**2 + (length_of_side/2)**2)**0.5
    num_of_sides *= 2

    if round(pi_archimedes, num+1) == round(pi_previous, num+1):
        break
        
    pi_previous = pi_archimedes

print(round(pi_archimedes, num))
