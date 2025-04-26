
def factorial_using_for_loop(number):
    print(f"inside the function with number: {number}")
    if number == 0:
        return 1

    factorial = 1
    
    for i in range(1, number + 1,1):
        print(f"inside the loop with i: {i}")
        factorial = factorial * i
    return factorial


number = abs(int(input("Enter a positive integer number: ")))

print(f"The factorial of {number} is {factorial_using_for_loop(number=number)}")