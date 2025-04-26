#Develop a Factorial project with at least one class

class Factorial:
    number = 1
    
    def __init__(self, number):
        self.number = number
        
    def factorial_using_for_loop(self):
        print(f"inside the function with number: {self.number}")
        if self.number == 0:
            return 1

        factorial = 1
        
        for i in range(1, number + 1,1):
            print(f"inside the loop with i: {i}")
            factorial = factorial * i
        return factorial


number = abs(int(input("Enter a positive integer number: ")))
factorial = Factorial(number)

print(f"The factorial of {number} is {factorial.factorial_using_for_loop()}")