import time
import sys

def print_slow(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
    print()

def start_game():
    print_slow("\n=== SYSTEM INITIALIZED: NEO-TOKYO NETRUNNER ===\n")
    time.sleep(0.5)
    print_slow("You wake up in a dim room. Cybernetic implants are buzzing in your head.")
    print_slow("Your monitor flashes: 'ICE Breaker detected an vulnerability in Megacorp mainframe.'")
    print_slow("You have two options to execute:")
    print("1) Launch a stealth brute-force attack on the server firewall.")
    print("2) Jack out of the net, grab your gear, and run before physical security traces you.")
    
    choice = input("\nEnter choice (1 or 2): ")
    
    if choice == "1":
        hack_sequence()
    elif choice == "2":
        escape_sequence()
    else:
        print_slow("\n[ERROR] Invalid input. Mainframe traced your hesitation. SYSTEM COMPROMISED.")

def hack_sequence():
    print_slow("\n[LOADING] Injecting malware packets into firewall...")
    for i in range(1, 4):
        print(f"Bypassing security node {i}/3...")
        time.sleep(1)
    
    print_slow("\n=== CRITICAL ALERT ===")
    print_slow("The admin password is encrypted. You mustguess the override frequency code!")
    print_slow("Hint: It is a number between 1 and 10.")
    
    attempts = 3
    secret_code = 7
    
    while attempts > 0:
        guess = int(input(f"\nEnter code (Attempts left: {attempts}): "))
        if guess == secret_code:
            print_slow("\n[SUCCESS] Encryption cracked! You downloaded 500,000 credits. You are a legendary netrunner.")
            return
        else:
            print_slow("[DENIED] Frequency offset wrong.")
            attempts -= 1
            
    print_slow("\n[FATAL] Admin locked you out. Megacorp sent a neural shockwave through your deck. GAME OVER.")

def escape_sequence():
    print_slow("\nYou rip the neural cables out of your neck and slam your deck shut.")
    print_slow("Footsteps echo down the hallway. Heavy boots. Corporate tactical team.")
    print("1) Jump out the fire escape window into the rainy neon neon alleyway.")
    print("2) Hide under your desk and hope their thermal scanners miss you.")
    
    choice = input("\nEnter choice (1 or 2): ")
    if choice == "1":
        print_slow("\nYou slide down the rusty escape pipe right into a waiting hover-cab. You got away clean!")
    else:
        print_slow("\nHiding under a desk against modern military tech? Bold strategy. They scanned your vitals instantly. BUSTED.")

# This actually kicks off the game logic
start_game()
import time
import sys
import random  # <-- Adds random number generator math

def print_slow(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)
    print()

# Initial inventory state tracking
player_inventory = ["Neural Deck"]

def start_game():
    print_slow("\n=== SYSTEM INITIALIZED: NEO-TOKYO NETRUNNER PRO ===\n")
    print_slow(f"Current Inventory: {player_inventory}")
    time.sleep(0.5)
    print_slow("\nYou are tracking a data package down a dark alley. A shady merchant offers you an item.")
    print("1) Buy a 'Laser-Decryptor' for 50 credits.")
    print("2) Ignore them and head straight to the mainframe node.")
    
    choice = input("\nEnter choice (1 or 2): ")
    if choice == "1":
        player_inventory.append("Laser-Decryptor")
        print_slow(f"\n[UPDATED] Added to gear. Inventory: {player_inventory}")
    
    print_slow("\nYou arrive at the Megacorp terminal block...")
    hack_sequence()

def hack_sequence():
    print_slow("\n[ALERT] Firewall engaged! Scanning for decryption tools...")
    time.sleep(1)
    
    # Logic check: Does the item exist in our list?
    if "Laser-Decryptor" in player_inventory:
        print_slow("\n[ITEM DETECTED] Your Laser-Decryptor bypasses the sub-layers automatically!")
        attempts = 5
    else:
        print_slow("\n[WARNING] Standard deck only. Security matrix is extremely tight.")
        attempts = 2
        
    # Generates a completely dynamic random code between 1 and 10
    secret_code = random.randint(1, 10)
    print_slow(f"Guess the system override frequency code between 1 and 10.")
    
    while attempts > 0:
        guess = int(input(f"\nEnter code (Attempts left: {attempts}): "))
        if guess == secret_code:
            print_slow("\n[SUCCESS] Mainframe completely broken! You are now a master netrunner.")
            return
        elif guess < secret_code:
            print_slow("[DENIED] Frequency too LOW.")
            attempts -= 1
        else:
            print_slow("[DENIED] Frequency too HIGH.")
            attempts -= 1
            
    print_slow(f"\n[FATAL] System locked. The correct code was {secret_code}. GAME OVER.")

start_game()
