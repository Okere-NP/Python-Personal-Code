# Program to display the Fibonacci sequence up to n-th term
fib_terms = int(input("How many fibonacci terms? "))

# Fibonacci Sequence list container
fill_list = []

# first two terms
fib1, fib2 = 0, 1
count = 0

# check if the number of terms is valid
if fib_terms <= 0:
   print("Please enter a positive integer")

# if there is only one term, return n1
elif fib_terms == 1:
   print("Fibonacci sequence upto" ,fib_terms, "is: ")
   print(fib1)

# generate fibonacci sequence
else:
   print("Fibonacci sequence:")
   while count < fib_terms:
      # Update the fill_list with new values of n1 in a list format
      fill_list.append(fib1)

      # next fib sequence after the addition of n1 and n2
      fibth = fib1 + fib2

      # update values
      fib1 = fib2
      fib2 = fibth
      count += 1

print(fill_list)