# Take a number as input
number = int(input("Enter a number: "))

# Check if the number is even or odd
if number % 2 == 0:
    print(number,"is Even.")
else:
    print(number,"is Odd.")

# Calculate and print the sum of all even numbers from 1 to the given number
sum_evens = 0
for i in range(1, number + 1):
    if i % 2 == 0:
        sum_evens += i

print("The sum of all even numbers from 1 to",number,"is:",sum_evens)