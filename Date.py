from datetime import datetime  

def calculate_age(birth_date_str):  
    try:  
        # Parse the input date  
        birth_date = datetime.strptime(birth_date_str, "%Y/%m/%d")  
        # Get the current date (fixed to 2019/02/01 for this example)  
        current_date = datetime(2024, 2, 1)  
        
        # Calculate age  
        age = current_date.year - birth_date.year  
        
        # Adjust for cases where the birthday hasn't occurred yet in the current year  
        if (current_date.month, current_date.day) < (birth_date.month, birth_date.day):  
            age -= 1  
            
        return age  
    except ValueError:  
        # If the date is not valid, return "WRONG"  
        return "WRONG"  

# Example input  
birth_date_input = input("Enter your birth date (yyyy/mm/dd): ")  
result = calculate_age(birth_date_input)  
print(result)

