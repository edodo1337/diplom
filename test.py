from cryptography.fernet import Fernet



# key = Fernet.generate_key()
key = b'BwiO91Mk77nvxEKsPwEl6KwQ_Xv2sva4rv9nmJuY0ig='
print(key)

f = Fernet(key)


# with open(filename, "r") as f_in:
#     data = f_in.read().encode()
#     crypted = f.encrypt(data)

#     f_out = open("internet2.txt", "w")
#     f_out.write(crypted.decode())
#     f_out.close()



with open(filename, "r") as f_in:
    data = f_in.read().encode()
    print(data)
    # crypted = f.encrypt(data)

    print(f.decrypt(data).decode())
    # f_out = open("internet2.txt", "w")
    # f_out.write(str(crypted))
    # f_out.close()