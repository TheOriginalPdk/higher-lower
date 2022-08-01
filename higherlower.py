from random import choice
from game_data import data 
from art import logo
from art import vs

#from replit import clear
playon = True 
while playon: 
    def compute(s):
        e=int(s)
        c = choice([i for i in range(0,51) if i not in [e]])
        x=int(c)
        global reserved_for_option_A
        # so the same item won't be selected for A & B
        reserved_for_option_A = int(x)
        name =(data[x]["name"])
        description = (data[x]["description"])
        country=(data[x]["country"])
        global follower_count
        #to be used to compare A & B and check if user answer is correct
        follower_count=(data[x]["follower_count"])
        a=(f"{name}, a {description}, from {country}")
        
        return a
    
    print(logo)
    a = compute(s=0)
    print(f"Compare A: {a}")
    follower_count_a=int(follower_count)
    # print(f"follower count A:{follower_count_a}")
    # print(f"reserved for option A:{reserved_for_option_A}")
    print(vs)
    b = compute(s=reserved_for_option_A)
    follower_count_b=int(follower_count)
    # print(f"follower count A:{follower_count_b}")
    print(f"Against B: {b}")

    user_guess=input("Who has more followers? Type 'A' or 'B': ").upper() 
    counter=0
    user_score = 0
    user_counter=0
    if user_guess=="A":
        user_counter=1
    elif user_guess=="B":
        user_counter=2
    if follower_count_a> follower_count_b:
        counter=1
    elif follower_count_b> follower_count_a:
        counter=2
    if user_counter==counter:
        # print("correct")
        user_score +=1
        print(f"You're right! Current score: {user_score}")
    else:
        # print("incorrect")
        print(f"Sorry, that's wrong. Final score: {user_score}")
    # cls() #this is clear for windows
    print("\033[H\033[J", end="") #this is clear for windows
    
    inside_loop = True
    while inside_loop:
        #clear() #this is clear for replit
        print("\033[H\033[J", end="") #this is clear for windows
        print(logo)
        print(f"You're right! Current score: {user_score}")
        a = compute(s=0)
        print(f"Compare A: {b}")
        #since if the first question is correct option b in the previous round becomes option a 
        follower_count_a=int(follower_count)
        # print(f"follower count A:{follower_count_a}")
        # print(f"reserved for option A:{reserved_for_option_A}")

        print(vs)
        b = compute(s=reserved_for_option_A)
        follower_count_b=int(follower_count)
        # print(f"follower count A:{follower_count_b}")
        print(f"Against B: {b}")

        user_guess=input("Who has more followers? Type 'A' or 'B': ").upper() 
        counter=0
        user_counter=0
        if user_guess=="A":
            user_counter=1
        elif user_guess=="B":
            user_counter=2
        if follower_count_a> follower_count_b:
            counter=1
        elif follower_count_b> follower_count_a:
            counter=2
        if user_counter==counter:
            # print("correct")
            user_score +=1
            print(f"You're right! Current score: {user_score}")
        else:
            # print("incorrect")
            print(f"Sorry, that's wrong. Final score: {user_score}")
            inside_loop = False
            playon = False


    