def main():  
    # Define genres  
    genres = ["Horror", "Romance", "Comedy", "History", "Adventure", "Action"]  
    genre_count = {genre: 0 for genre in genres}  

    # Get number of participants  
    n = int(input("Enter the number of participants: "))  
    
    for _ in range(n):  
        # Read participant's input  
        data = input().split()  
        name = data[0]  # This is the participant's name  
        preferred_genres = data[1:]  # These are the preferred genres  
        
        # Count the genres  
        for genre in preferred_genres:  
            if genre in genre_count:  
                genre_count[genre] += 1  

    # Sort genres by the number of interests (descending) and then by name (alphabetically)  
    sorted_genres = sorted(genre_count.items(), key=lambda x: (-x[1], x[0]))  

    # Print the results  
    for genre, count in sorted_genres:  
        print(f"{genre} : {count}")  

if __name__ == "__main__":  
    main()