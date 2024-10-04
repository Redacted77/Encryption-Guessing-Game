class encryption_1:
    def __init__(self,word): # important variables
        self.word = word     # the message
        self.re_key1 = [0]   # reverse keys for the sublevel in each key
        self.re_key2 = [0]
        self.re_key3 = [0] 
        self.send_back = [0]
        self.num_list = [0]  # stores the ASC of the letters
        self.num  = len(self.word)     # get the length of the word
        for y in range(1, self.num):
            self.num_list.append(0)
            self.re_key1.append(0)
            self.re_key2.append(0)
            self.re_key3.append(0)
            self.send_back.append(0)
    def encrypt_1(self):     # the encryption type 1 method
        key1 = 7             # keys should have been defined outside of the method
        key2 = 4
        key3 = 2
        position = 0         # position of the each character of the message in the alphabet
        # level 1 encryption (adds 7 to the ASC of the letters)

        for k0 in range(1, self.num+1):
            char = self.word[k0-1]        # turns the string to char
            message = ord(char) - 96      # suptracts 96 to get the position of the letters
            position = message + key1
            while position > 26:          # sublevel 1 encryption (loops every time it's past z back to a)
                self.re_key1[k0-1] = self.re_key1[k0-1]+1 # keeps track of how many times it subtracts 26
                position -= 26
                
            self.num_list[k0-1] = position

        # level 2 encryption (multiples the result of the last encryption by 4)

        for k1 in range(1, self.num+1):
            self.num_list[k1-1] = self.num_list[k1-1] * key2
            while self.num_list[k1-1] > 26:                  # sublevel 2 (-26 for as long as the multiplied number is greater than 26)
                self.re_key2[k1-1] = self.re_key2[k1-1] + 1
                self.num_list[k1-1] -= 26

        # level 3 encryption (power 2 of the result of the last encryption)

        for k2 in range(1, self.num+1):                           
            self.num_list[k2-1] = self.num_list[k2-1] ** key3
            while self.num_list[k2-1] > 26:                  # sublevel 3 (same as sublevel 2)
                self.re_key3[k2-1] = self.re_key3[k2-1]+1
                self.num_list[k2-1] -= 26
        for b in range(1, self.num+1):                            # prints the encrypted word
            print(chr(self.num_list[b-1] + 96), end="")
    def decrypt_1(self):           # the decryption type 1 method

        # decryption level 1 (reverse encryption level 3, using ̶r̶o̶o̶t̶2 power 0.5) 

        for re_k0 in range(1, self.num+1): 
            while self.re_key3[re_k0-1] > 0:    # de_suplevel 1 adds 26 that were subtracted from sublevel 3 (using re_key3)
                self.num_list[re_k0-1] += 26
                self.re_key3[re_k0-1] -= 1
            self.num_list[re_k0-1] = int(self.num_list[re_k0-1] ** 0.5)

        # decryption level 2 (reverse encryption level 2, divide by 4)

        for re_k1 in range(1, self.num+1):
            while self.re_key2[re_k1-1] > 0:    # same as de_sublevel 1 (using re_key2)
                self.num_list[re_k1-1] += 26
                self.re_key2[re_k1-1] -= 1
            self.num_list[re_k1-1] = self.num_list[re_k1-1] / 4

        # decryption level 3 (reverse encryption level 1, add 7)

        for re_k2 in range(1, self.num+1):
            while self.re_key1[re_k2-1] > 0:   # same as before (re_key1)
                self.num_list[re_k2-1] += 26
                self.re_key1[re_k2-1] -= 1
            self.num_list[re_k2-1] -= 7
        for b in range(1, self.num+1):
            og = int(self.num_list[b-1]) + 96
            self.send_back[b-1] = chr(og)          # prepares the original message
        self.send_back = "".join(self.send_back)
        return self.send_back
class encryption_2:
    def __init__(self, word):        # improtant variables
        self.word = word
        self.length = len(self.word)
        self.count = 0
        self.counter = [0]
        self.key_list = [0]
        self.send_back = [0]
        for y in range(1, self.length):    
            self.counter.append(0)
            self.key_list.append(0)
            self.send_back.append(0)

    def key_formula(self, number):          # the cypher n x r^2  / 2 (n is the ACS code, r is the lenght of the word given)
        self.count = 0
        result = number * self.length ** 2
        result = result / 2
        while result > 26:
            result = result - 26
            self.count = self.count + 1         # counts how many time we subtract 26
        return result                           # returns the position of the encrypted charecter 
    
    def encrypt_2(self):
        for x in range(1, self.length+1):       # for loop to call the cypher and keep track of how many time we subtracted 26
            char = self.word[x-1]
            message = ord(char) - 96            # gets the opsition of the characters in the original message
            keys = self.key_formula(message)
            self.key_list[x-1] = keys
            keys = int(keys)
            print(chr(keys + 96), end="")       # prints the encrypted message
            self.counter[x-1] = self.count
    def decrypt_2(self):
        for k in range(0, self.length):         # reverses the process key_formula
            while self.counter[k] > 0:
                self.key_list[k] = self.key_list[k] + 26
                self.counter[k] -= 1
            self.key_list[k] = self.key_list[k] * 2
            self.key_list[k] = self.key_list[k] / self.length ** 2
            self.key_list[k] = int(self.key_list[k])
            self.send_back[k] = chr(self.key_list[k] + 96)       # prepares the original message
        self.send_back = "".join(self.send_back)
        return self.send_back
class encryption_3:
    def __init__(self,word):          # important variables
        self.word = word
        self.length = len(self.word)
        self.num_list = [0]
        self.reverse = [0]
        self.og = [0]
        self.counter = [0]
        self.send_back = [0]
        for x in range(1, self.length):
            self.num_list.append(0)
            self.reverse.append(0)
            self.counter.append(0)
            self.og.append(0)
            self.send_back.append(0)
        for i in range(0, self.length):       # chareacters of the original message
            char = ord(self.word[i])
            self.num_list[i] = char - 96

    def encrypt_3(self):                            # n` if %2 = 0 then add 3
        for l in range(0, len(self.word)):          # creats a reversed list of the original charecters
            self.reverse[l] = self.num_list[self.length - (l + 1)]
        for loops in range(0, self.length):         # checks if the position of the charecter in the list can be divided by 2
            if (loops % 2) == 0:                    # if so it will add 3 to it's posistion in the alphabet NOT the list
                self.reverse[loops] = self.reverse[loops] + 3
                while self.reverse[loops] > 26:
                    self.reverse[loops] = self.reverse[loops] - 26
                    self.counter[loops] = self.counter[loops] + 1
            print(chr(self.reverse[loops] + 96), end="")
    
    def decrypt_3(self):                            # reverses the process of encrypt_3
        for ln in range(0, self.length):
            while self.counter[ln] > 0:
                self.reverse[ln] = self.reverse[ln] + 26
                self.counter[ln] = self.counter[ln] - 1
            if ln % 2 == 0:
                self.reverse[ln] = self.reverse[ln] - 3
        for op in range(0, self.length):
            self.og[op] = self.reverse[self.length - (op + 1)]
            self.send_back[op] = chr(self.og[op] + 96)
        self.send_back = "".join(self.send_back)    # prepares the original message
        return self.send_back
class call_to_arms:         # calls the encryption & decryption after it splits the message and prints it
    def __init__(self,space):
        self.no_space = space
        self.right_value = 0
        self.decrypted = [0]
        for b in range(0, len(self.no_space)-1):
            self.decrypted.append(0)
    
    def d_print(self):
        length = len(self.no_space)
        print("Decrypted: ", end="")
        for x in range(0, length):
            print(str(self.decrypted[x]), end="")
            print(" ", end="")
        print("")

    def try_1(self):                        # encryption 1
        length = len(self.no_space)
        print("encrypted: ", end="")
        for x in range(0, length):
            word = self.no_space[x]
            p2 = encryption_1(word)
            p2.encrypt_1()
            self.decrypted[x] = p2.decrypt_1()
            print(" ", end="")
        print("")
        self.d_print()
        self.right_value = 7
        return self.right_value
    
    def try_2(self):                        # encryption 2
        length = len(self.no_space)
        print("encrypted: ", end="")
        for x in range(0, length):
            word = self.no_space[x]
            p3 = encryption_2(word)
            p3.encrypt_2()
            self.decrypted[x] = p3.decrypt_2()
            print(" ", end="")
        print("")
        self.d_print()
        self.right_value = 6
        return self.right_value
    
    def try_3(self):                        # encryption 3
        length = len(self.no_space)
        print("encrypted: ", end="")
        for x in range(0, length):
            word = self.no_space[x]
            p4 = encryption_3(word)
            p4.encrypt_3()
            self.decrypted[x] = p4.decrypt_3()
            print(" ", end="")
        print("")
        self.d_print()
        self.right_value = 5
        return self.right_value

import time
import random

def right_answer(right_value):
    print("""what's the cypher/key for this encryption:
          A. reverses your message, checks if it's position(in the message) is even, if so adds 3 to it's position(in the alphabet).
          B. goes letter by letter and multiples the position(in the alphabet) by the length of your message.
          C. position of the letter + 7
          D. position of each letter + it's position(in the message)
          E. adds 7 to it's position(in the alphabet) then multiples that by 4 then ^2 to the result. """)
    user_value = input()
    user_value = user_value.lower()
    if user_value == 'a':
        user_value = 5
    elif user_value == 'b':
        user_value = 6
    elif user_value == 'e':
        user_value = 7
    if user_value == right_value:
        print("That's Correct")
        exit(0)
    else:
        print("That's Wrong")
        exit(0)

def options(word, respons):        # tells call_to_arms which encryption to use based on the respose from the user
    op = call_to_arms(word)
    if respons == 1:
        right_value = op.try_1()
        right_answer(right_value)
    elif respons == 2:
        right_value = op.try_2()
        right_answer(right_value)
    elif respons == 3:
        right_value = op.try_3()
        right_answer(right_value)

def intro():
    i = 9
    ii = 0
    c = 9
    for y in range(1, 9):
        while i > ii:
            print(" ", end="")
            i = i-1
        for x in range(0, y):
            print("#", end="")
        for t in range(0, 4):
            print(" ", end="")
        for x in range(0, y):
            print("#", end="")
        print("")
        c = c - 1
        i = c
        if y == 4:
             print("Encryption Guessing Game")
        time.sleep(0.5)    

intro()
t = time.localtime(time.time())
word = input("Enter your message: ")
word = word.lower()
no_space = word.split()              # splits the message based on spaces
for num in range(0, len(no_space)):
    check = no_space[num].isalpha()
    if check == True:
        pass
    else:
        print("Error: can't have sympols or numbers in your message")
        exit(0)

print("""how do you want to encrypt it:
there are three types of encryptions: 1, 2 and 3 for encryptions 1 - 3
or
a. a random one from the three.
b. pick one based on my current time.""")

respons = input()
time.sleep(0.5)
#  sends the value (1-3) that will indcate which encryption of the 3 we will use
if respons == 'a':                # send a random number from 1-3
    random_ = random.randint(1, 3)
    options(no_space, random_)
elif respons == 'b':              #  working with 12-hour system from 1-4 sends value of 1 and so on
    hour = t.tm_hour
    value = 0
    if 1 >= hour >= 4:
        value = 1
        options(no_space, value)
    elif 5 >= hour >= 8:
        value = 2
        options(no_space, value)
    else:
        value = 3
        options(no_space, value)
for x in range(1,4):
    if respons == str(x):
        options(no_space, x)

else:
    print("error: next time select one of the options :)")
    exit(0)
