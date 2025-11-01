ratings = []
while (ratings_input := input("Enter a rating (1-5) or 'exit' to quit: ")): 
    if ratings_input == 'exit': 
        break
    else:
        try:
            #This will transform the input to an integer
            rating = int(ratings_input) 
            if rating < 1 or rating > 5: 
                print("Invalid input. Please enter a number between 1 and 5 or 'exit'") 
                continue 
            
            ratings.append(rating)
            
            if rating==5: 
                print("Feedback: Excellent") 
            elif rating==4: 
                print("Feedback: Good") 
            elif rating==3: 
                print("Feedback: Average") 
            elif rating==2: 
                print("Feedback: Poor") 
            else: 
                print("Feedback: Terrible") 
        except ValueError: 
            print("Invalid input. Please enter a number between 1 and 5 or 'exit'")

if ratings:
    avg_score=sum(ratings)/len(ratings)

print()    
print (f"Survey ended. You collected {len(ratings)} ratings. Average score: {avg_score:.1f}")
