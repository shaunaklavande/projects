#Shaunak Lavande

class FibonacciGenerator:
    def __init__(self, n):
        self.n = n

    def generate_sequence(self):
        if self.n <= 0:
            return []
        elif self.n == 1:
            return [1]
        elif self.n == 2:
            return [1, 1]
        else:
            sequence = [1, 1]
            while len(sequence) < self.n:
                next_number = sequence[-1] + sequence[-2]
                sequence.append(next_number)
            return sequence

def main():
    n = int(input("Enter the number of Fibonacci numbers to generate: "))
    
    if n <= 0:
        print("Please enter a positive integer.")
        return
    
    generator = FibonacciGenerator(n)
    sequence = generator.generate_sequence()
    
    print("Fibonacci sequence:")
    for num in sequence:
        print(num, end=", ")

if __name__ == "__main__":
    main()
