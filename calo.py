''' 4.2 calo per minute loss
prog loss in 10, 15, 20, 25, 30 minutes
'''

def calories_burned():
    
    calories_loss_perminute = 4.2
    
    for fat in range (10, 36, 5):
        burned = (fat / 1) + calories_loss_perminute
        print(f'Calories {fat}: {burned}')
    
    
    
calories_burned()