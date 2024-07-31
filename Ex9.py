def calculate_points_and_wins():  
    total_points = 0  
    total_wins = 0  
    
    for match in range(30):  
        points = int(input())
        
        # Validate input  
        if points not in [0, 1, 3]:  
            print("Invalid input! Please enter 0, 1, or 3.")  
            return  
        
        total_points += points  
        
        if points == 3:  
            total_wins += 1  
            
    print(total_points , total_wins) 
       
       
calculate_points_and_wins() 