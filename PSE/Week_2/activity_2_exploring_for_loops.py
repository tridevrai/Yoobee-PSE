# Activity 2: 
# Write a code to calculate the factorial of a number using for loop
# The factorial of a number is the product of all positive integers less than or equal to that number
# For example, the factorial of 5 is 5 * 4 * 3 * 2 * 1 = 120
# The factorial of 0 is 1
# n! = n * (n-1) * (n-2) * ... * 1

def factorial_using_for_loop(number):
    print(f"inside the function with number: {number}")
    if number == 0:
        return 1

    # factorial of 0 is 1
    factorial = 1
    for i in range(2, number + 1,1):
        print(f"inside the loop with i: {i}")
        factorial = factorial * i
    return factorial


number = abs(int(input("Enter a positive integer number: ")))

print(f"The factorial of {number} is {factorial_using_for_loop(number=number)}")