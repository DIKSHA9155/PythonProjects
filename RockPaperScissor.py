import random
print("""
  o__ __o                                o        o__ __o                                                     o__ __o                  o                                              
 <|     v\                              <|>      <|     v\                                                   /v     v\               _<|>_                                            
 / \     <\                             / \      / \     <\                                                 />       <\                                                               
 \o/     o/       o__ __o        __o__  \o/  o/  \o/     o/   o__ __o/  \o_ __o      o__  __o   \o__ __o   _\o____            __o__    o        __o__    __o__   o__ __o    \o__ __o  
  |__  _<|       /v     v\      />  \    |  /v    |__  _<|/  /v     |    |    v\    /v      |>   |     |>       \_\__o__     />  \    <|>      />  \    />  \   /v     v\    |     |> 
  |       \     />       <\   o/        / \/>     |         />     / \  / \    <\  />      //   / \   < >             \    o/         / \      \o       \o     />       <\  / \   < > 
 <o>       \o   \         /  <|         \o/\o    <o>        \      \o/  \o/     /  \o    o/     \o/         \         /   <|          \o/       v\       v\    \         /  \o/       
  |         v\   o       o    \\         |  v\    |          o      |    |     o    v\  /v __o   |           o       o     \\          |         <\       <\    o       o    |        
 / \         <\  <\__ __/>     _\o__</  / \  <\  / \         <\__  / \  / \ __/>     <\/> __/>  / \          <\__ __/>      _\o__</   / \   _\o__</  _\o__</    <\__ __/>   / \       
                                                                        \o/                                                                                                           
                                                                         |                                                                                                            
                                                                        / \                                                                                                                                                                                                                                                                        
""")
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice >= 0 and user_choice <= 2:
    print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif computer_choice > user_choice:
    print("You lose!")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice == user_choice:
    print("It's a draw!")
