def is_prime(n):  
    if n <= 1:  
        return False  
    for i in range(2, int(n**0.5) + 1):  
        if n % i == 0:  
            return False  
    return True  

def count_prime_divisors(num):  
    prime_divisors = set()  
    for i in range(2, num + 1):  
        if num % i == 0 and is_prime(i):  
            prime_divisors.add(i)  
    return len(prime_divisors)  

def main():  
    numbers = []  
    
    # Read 10 numbers from input  
    for _ in range(10):  
        num = int(input("Enter a number: "))  
        numbers.append(num)  

    max_count = -1  
    result_number = None  
    
    # Process each number  
    for number in numbers:  
        count = count_prime_divisors(number)  
        
        # Check if we need to update the result  
        if count > max_count or (count == max_count and (result_number is None or number > result_number)):  
            max_count = count  
            result_number = number  

    # Print the result  
    if result_number is not None:  
        print(f"The number with the most prime divisors is: {result_number} with {max_count} prime divisors.")  
    else:  
        print("No prime divisors found.")  

if __name__ == "__main__":  
    main()