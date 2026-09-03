import time

print("Initializing bypass sequence...")
time.sleep(1)

for i in range(1, 6):
    print(f"Loading data stream {i}/5... [OK]")
    time.sleep(0.5)

print("\nAccess Granted. You are fully operational.")
