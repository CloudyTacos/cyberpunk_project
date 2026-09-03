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
