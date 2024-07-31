def calculate_points_and_wins():  
    total_points = 0  
    total_wins = 0  
    
    print("Enter the points for each of the 30 matches (0 for loss, 1 for draw, 3 for win):")  
    
    for match in range(30):  
        points = int(input(f"Match {match + 1}: "))  
        
        # Validate input  
        if points not in [0, 1, 3]:  
            print("Invalid input! Please enter 0, 1, or 3.")  
            return  
        
        total_points += points  
        
        if points == 3:  # Increment wins count for a win  
            total_wins += 1  
            
    print(f"Total Points: {total_points}")  
    print(f"Total Wins: {total_wins}")  

# Run the function  
calculate_points_and_wins() 