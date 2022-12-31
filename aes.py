import os
from secrets import token_bytes
from Cryptodome.Cipher import AES

def generate_key():
    key = token_bytes(32)
    filepath = "./key.bin"

    with open(filepath, "wb") as file:
        file.write(key)

def open_key(): 
    filepath = "./key.bin"

    with open(filepath, "rb") as file:
         return file.read()

def encrypt(website, username, password):
    filepath = "./data.txt"

    #opens key
    key = open_key()
    details = []

    #verify unique website in data file
    if os.path.isfile(filepath):
        with open(filepath, "r") as file:
            for line in file:
                #split file
                line_data = line.split(', ')

                #finds website
                if line_data[0] == website:
                    return False

    #encryption
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    encrypted_data, tag = cipher.encrypt_and_digest(password.encode("ascii"))

    #append data to details
    details.append(website)
    details.append(username)

    #convert binary to hex
    details.append(encrypted_data.hex())
    details.append(tag.hex())
    details.append(nonce.hex())

    #write to data file
    with open (filepath, "a") as file:
        file.write(', '.join(str(s) for s in details) + '\n')

    return encrypted_data, tag, nonce

def decrypt(website): 
    filepath = "./data.txt"

    #open data file
    with open(filepath, "r") as file:
        
        for line in file:
            #split file
            line_data = line.split(', ')

            #finds website
            if line_data[0] == website:
                website = line_data[0]
                username = line_data[1]
                encrypted_data = bytes.fromhex(line_data[2])
                tag = bytes.fromhex(line_data[3])
                nonce = bytes.fromhex(line_data[4])

                #decrypt plain text
                key = open_key()
                cipher = AES.new(key, AES.MODE_EAX, nonce)
                password = cipher.decrypt(encrypted_data)

                try:
                    cipher.verify(tag)
                    return username, password.decode("ascii")

                except:
                    return False