# Define a function to calculate sums of even and odd numbers
def calculate_even_odd_sums(numbers):
    sum_even = 0
    sum_odd = 0

    for num in numbers:
        if num % 2 == 0:
            sum_even += num
        else:
            sum_odd += num

    return sum_even, sum_odd


# Example usage
numbers = [1, 2, 3, 4, 5, 6]
sum_even, sum_odd = calculate_even_odd_sums(numbers)

print("Sum of even numbers:",sum_even)
print("Sum of odd numbers:",sum_odd)
