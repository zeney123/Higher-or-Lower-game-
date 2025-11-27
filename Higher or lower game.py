import random
from Data import data
vs = r"""
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""
logo = r"""
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

game = True
score = 0

first_value = random.choice(data)
print(logo)
while game:
    second_value = random.choice(data)
    while second_value == first_value:
        second_value = random.choice(data)

    print(f"Compare A: {first_value['name']}, a {first_value['description']}, from {first_value["country"]}\n")
    print(vs)
    print(f"Compare B: {second_value["name"]}, a {second_value["description"]}, from {second_value["country"]}\n")
    more_followers= input("Who has more followers? Type 'A' or 'B' ").upper()
    if (more_followers=="A" and first_value["follower_count"]> second_value["follower_count"]) \
        or (more_followers=="B" and second_value["follower_count"]> first_value["follower_count"]):
            score+=1
            print(logo)

            print(f"You're right! Current score: {score}")

            first_value=second_value
    else:
            print(f"\naSorry, that's wrong. Final score: {score}")
            game=False
            repeat=input("\nDo you want to play again? Type 'y' for yes or 'n' for no: ").lower()
            if repeat=="y":

                game =True
            elif repeat=="n":
                print("Thanks for playing my game!")
                game= False