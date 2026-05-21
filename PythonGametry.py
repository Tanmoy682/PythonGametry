import random
import time

def slow_print(text):
    print(text)
    time.sleep(1)

def battle(player_hp):
    enemy_hp = 30
    slow_print("\n🚨 An alien pirate appears!")

    while enemy_hp > 0 and player_hp > 0:
        print(f"\nYour HP: {player_hp} | Enemy HP: {enemy_hp}")
        print("1. Attack ⚔️")
        print("2. Block 🛡️")
        print("3. Heal 💊")

        choice = input("Choose action: ")

        enemy_attack = random.randint(5, 12)

        if choice == "1":
            dmg = random.randint(8, 15)
            enemy_hp -= dmg
            slow_print(f"You deal {dmg} damage!")

            player_hp -= enemy_attack
            slow_print(f"The enemy hits you for {enemy_attack}!")

        elif choice == "2":
            reduced = max(0, enemy_attack - random.randint(5, 10))
            player_hp -= reduced
            slow_print(f"You block! You only take {reduced} damage.")

        elif choice == "3":
            heal = random.randint(8, 14)
            player_hp += heal
            player_hp -= enemy_attack
            slow_print(f"You heal for {heal}, but take {enemy_attack} damage!")

        else:
            slow_print("You hesitate... and get hit!")
            player_hp -= enemy_attack

    return player_hp

def start_game():
    player_hp = 50

    slow_print("🚀 You wake up aboard the starship AURORA...")
    slow_print("Something has gone terribly wrong.")

    while True:
        print("\nWhat do you do?")
        print("1. Check the bridge 🧭")
        print("2. Go to the engine room 🔧")
        print("3. Search the cargo bay 📦")

        choice = input("> ")

        if choice == "1":
            slow_print("\nYou head to the bridge...")
            slow_print("The ship is drifting through unknown space.")
            player_hp = battle(player_hp)

        elif choice == "2":
            slow_print("\nThe engine room is unstable...")
            event = random.choice(["repair", "explosion"])

            if event == "repair":
                slow_print("You stabilize the engine and recover energy!")
                player_hp += 10
            else:
                slow_print("A plasma burst hits you!")
                player_hp -= 15

        elif choice == "3":
            slow_print("\nYou find a mysterious alien artifact...")
            slow_print("It restores your strength.")
            player_hp += 20

        else:
            slow_print("You wander aimlessly and lose time...")

        if player_hp <= 0:
            slow_print("\n💀 You have died in deep space...")
            break

        if player_hp >= 100:
            slow_print("\n🌟 You found a way to stabilize the ship and escape!")
            slow_print("YOU WIN!")
            break

        slow_print(f"\nCurrent HP: {player_hp}")

if __name__ == "__main__":
    start_game()

