class keyword_cipher(object):
    def __init__(self, abc, keyword):
        self.abc = abc
        self.key_abc = "".join(dict.fromkeys(keyword + abc))
        self.enc_table, self.dec_table = str.maketrans(
            self.abc, self.key_abc), str.maketrans(self.key_abc, self.abc)
        
    def encode(self, plain):
        return plain.translate(self.enc_table)

    def decode(self, ciphered):
        return ciphered.translate(self.dec_table)

abc = "abcdefghijklmnopqrstuvwxyz"
key = "keyword"

cipher = keyword_cipher(abc, key)

print(cipher.encode("xyz"))
print(cipher.decode("key"))