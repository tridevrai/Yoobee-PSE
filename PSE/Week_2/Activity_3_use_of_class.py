#Develop a Factorial project with at least one class

class FactorialCalculator:
        
    def __init__(self, number):
        self.number = number
        
    def factorial_using_for_loop(self):
        print(f"inside the function with number: {self.number}")
        if self.number == 0 or self.number == 1:
            return 1

        factorial = 1
        
        for i in range(1, number + 1,1):
            print(f"inside the loop with i: {i}")
            factorial = factorial * i
            
        return factorial

class PrimeNumberChecker:
    def __init__(self,number):
        self.number = number

    def is_prime(self):
        if self.number < 0:
            return False
        if self.number == 0 or self.number == 1:
            return False
        else:
            factors_counter = 1
            
            for i in range(2, self.number+1):
                if (self.number % i == 0):
                    factors_counter = factors_counter + 1
                if(factors_counter > 2):
                    return False
            
            if(factors_counter == 2):
                return True
            else:
                return False


number = abs(int(input("Enter a positive integer number: ")))

factorial = FactorialCalculator(number)
prime_number = PrimeNumberChecker(number)

print(f"The factorial of {number} is {factorial.factorial_using_for_loop()}")
print(f"The number {number} is prime: {prime_number.is_prime()}")