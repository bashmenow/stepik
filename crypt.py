import simplecrypt
with open("encrypted.bin", "rb") as inp, open("passwords.txt", 'r') as pwd:
    encrypted = inp.read()
    for p in pwd:
        try:
            data = simplecrypt.decrypt(p.rstrip(), encrypted)
        except simplecrypt.DecryptionException:
            continue
        else:
            print(data.decode('utf-8'))