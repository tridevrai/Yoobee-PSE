# Activity 3: Deadline 2 May
# rewrite below sample code (from activity w3-6)
# without using initializer & self (if it is possible?)


class Factorial:

    def factorial(self, num1):

        result = 1  # Initialized before the loop to store the product.

        for i in range(1, num1 + 1):

            result *= i

        return result

    def check_prime(self, num1):  # Prime check method added

        if num1 < 2:  # 0 and 1 are not prime numbers

            return False

        for i in range(
            2, int(num1**0.5) + 1
        ):  # Check up to the square root of num1 and int to make it not show decimal values

            # Check if num1 is divisible by i

            if num1 % i == 0:

                return False

        return True

    def display(self, num1):  # Display method corrected

        print("Factorial of", num1, "is", self.factorial(num1))

        if self.check_prime(num1):

            print(f"{num1} is a prime number.")

        else:

            print(f"{num1} is not a prime number.")


calculator = Factorial()
calculator.display(10)
