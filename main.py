from art import logo, vs
from game_data import data
from replit import clear
import random
game_over = False
score = 0

def account(info):
  account_name = info['name']
  account_description = info['description']
  account_country = info['country']
  return(f"{account_name}: a {account_description} from {account_country}")
  
print(logo)
prev_option = None

while game_over == False:
  random_int_1 = random.randint(0, len(data) - 1)
  option_a = data[random_int_1]
  random_int_2 = random.randint(0, len(data) - 1)
  option_b = data[random_int_2]
  if option_a == option_b:
    random_int_3 = random.randint(0, len(data) - 1)
    option_b = data[random_int_3]
  if prev_option != None:
        option_a = prev_option

  print(f"Who has more followers?\nOption A: {account(option_a)}")
  
  print(vs)
  
  choice = input(f"Option B: {account(option_b)} (Type 'A' or 'B')\n").lower()

  clear()
  print(logo)
  
  if choice == "a" and option_a['follower_count'] > option_b['follower_count']:
    score +=1
    print(f"Correct! Current score: {score}")
    prev_option = option_a
  elif choice == "b" and option_a['follower_count'] < option_b['follower_count']:
    score +=1
    print(f"Correct! Current score: {score}")
    prev_option = option_b
  else:
    print(f"Game Over. Your score: {score}")
    game_over = True
