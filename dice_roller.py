import random
import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def dice_animation():
    animation = ['Rolling.', 'Rolling..', 'Rolling...']
    for i in range(3): 
        clear_screen()
        print(animation[i % len(animation)])
        time.sleep(0.5)

def roll_dice():
    input("🎲 Press Enter to roll the die...")
    dice_animation()
    result = random.randint(1, 6)
    print(f"\n🎉 You rolled a {result}!")

if __name__ == "__main__":
    while True:
        roll_dice()
        again = input("\nDo you want to roll again? (y/n): ").strip().lower()
        if again != 'y':
            print("Goodbye!")
            break
