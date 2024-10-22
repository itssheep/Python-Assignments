#In this assignment the user inputs a message which is then encoded using the table below using a shift cipher.


table =[['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm'], 
['o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'n', 'm', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l'], 
['p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'n', 'o', 'l', 'm', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k'], 
['q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'n', 'o', 'p', 'k', 'l', 'm', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'], 
['r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'n', 'o', 'p', 'q', 'j', 'k', 'l', 'm', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'], 
['s', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'n', 'o', 'p', 'q', 'r', 'i', 'j', 'k', 'l', 'm', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'], 
['t', 'u', 'v', 'w', 'x', 'y', 'z', 'n', 'o', 'p', 'q', 'r', 's', 'h', 'i', 'j', 'k', 'l', 'm', 'a', 'b', 'c', 'd', 'e', 'f', 'g'], 
['u', 'v', 'w', 'x', 'y', 'z', 'n', 'o', 'p', 'q', 'r', 's', 't', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'a', 'b', 'c', 'd', 'e', 'f'], 
['v', 'w', 'x', 'y', 'z', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'a', 'b', 'c', 'd', 'e'], 
['w', 'x', 'y', 'z', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'a', 'b', 'c', 'd'], 
['x', 'y', 'z', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'a', 'b', 'c'], 
['y', 'z', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'a', 'b'], 
['z', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'a']] 



## Start writing you code below

# Step 1: Input checks and constants
key2 = ''
mIndex = 0
eMsg = ''
t = False  

while not t:  
    msg = input('Enter the message: ') # Input message

    for i in msg: # checks if characters in message are all alphabetical, if not it will continue to prompt the user
        if i.isalpha() == True:
            t = True 

t = False

while not t:
    key = input('Enter the key: ') # Input key

    for i in key: # checks if characters in key are all alphabetical, if not it will continue to prompt the user
        if i.isalpha() == True:
            t = True
        elif i == ' ': # if char is a space re-prompt user (not covered by isalpha)
            t = False
            break
        else:
            t = False
    

# Step 2: Change uppers to lowers and remove special characters


key = key.lower()
msg = msg.lower()
cleankey = ''
cleanmsg = ''
for i in key:
    if i.isspace() or i.isalpha():
        cleankey += i

for i in msg:
    if i.isspace() or i.isalpha():
        cleanmsg += i

key = cleankey
msg = cleanmsg

# Step 3: Get appropriate length of key & remove spacing


mnSpace = msg.replace(' ', '') # removes spaces in msg to set cipher key length properly

while len(key2) < len(mnSpace): # sets cipher key length to the msg length 
    key2 += key

# Step 4: Match spacing for msg & key

newkey = '' 
for char in msg: # iterates through msg and correctly orders/spaces cipher key
    if char == ' ':  # if there is a space, add a space to the key
        newkey += ' '
    else: # else if there isnt a space
        newkey += key2[0] # add the first character of key2 to the newkey
        key2 = key2[1:] # slices char to continue iteration

key = newkey 
# Step 5: Encrypt using table

for c in key:

    m = msg[mIndex] # gets number of char in msg

    if m == ' ': # if theres a space, add a space to the encrypted message
        eMsg += ' '
        
    else:
        num = ord(c) - ord('a') + 1 # gives us which letter we are currently iterating through

        rowNum = (num-1)//2 # calculates row # (left/right)
        
        colNum = ord(m) - ord('a')  # gives us column number (up/down)
           
        eChar = table[rowNum][colNum] # finds the character in the table then adds to our encrypted message
        eMsg += eChar
    mIndex = (mIndex + 1)%len(msg) # ensures that we will not go out of range of msg

    print(f'Encrypted Message is {eMsg}')
