#Program to output a combination when the right 6-digit letters is read from user
import time
key = 'BKPJ'
combo = "Santa Clause"
x = 1
y = 0
z = 0

print("Establishing server connection", end="", flush = True)
while(y < 5):
    time.sleep(1)
    print(".", end="", flush = True)
    y += 1
print("[Connected to 192.168.4.52]")
time.sleep(2)

while(x):
    print("Please enter the four digit key?")
    if input() == key:
        print("Access Granted")
        time.sleep(2)
        print("The key is located in the [", end="", flush = True)
        print(combo[0], end="", flush = True)
        time.sleep(.3)
        print(combo[1], end="", flush = True)
        time.sleep(.3)
        print(combo[2], end="", flush = True)
        time.sleep(.3)
        print(combo[3], end="", flush = True)
        time.sleep(.3)
        print(combo[4], end="", flush = True)
        time.sleep(.7)
        print(" ", end="", flush = True)
        time.sleep(.7)
        print(combo[6], end="", flush = True)
        time.sleep(.3)
        print(combo[7], end="", flush = True)
        time.sleep(.3)
        print(combo[8], end="", flush = True)
        time.sleep(.3)
        print(combo[9], end="", flush = True)
        time.sleep(.3)
        print(combo[10], end="", flush = True)
        time.sleep(.3)
        print(combo[11], end="", flush = True)
        time.sleep(.3)
        print("]", end="", flush = True)
        
        x = 0
        time.sleep(3)
        print("")
    else:
        print("error, incorrect key")
        
print("Exiting to main terminal", end="", flush = True)
while(z < 5):
    time.sleep(1)
    print(".", end="", flush = True)
    z += 1
print("[Connection terminated]")
time.sleep(2)
      

 

