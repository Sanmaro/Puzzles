class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self._key = key
        self._alphabet = alphabet
    
    
    def encode(self, text):
        self._pass = (self._key[:len(text)] 
                      if len(text) <= len(self._key) 
                      else (self._key * ((len(text) // len(self._key)) + 1))
                            [:len(text)])
        
        self._ciphered = ""

        for i in range(len(text)):
            if text[i] in self._alphabet:
                diff = (self._alphabet.find(text[i]) 
                    + (self._alphabet.find(self._pass[i])))
                if diff >= len(self._alphabet):
                    diff -= len(self._alphabet)
                self._ciphered += self._alphabet[diff]
            else:
                self._ciphered += text[i]

        return self._ciphered
    

    def decode(self, text):
        self._pass = (self._key[:len(text)] 
                if len(text) <= len(self._key) 
                else (self._key * ((len(text) // len(self._key)) + 1))
                        [:len(text)])
        
        self._deciphered = ""

        for i in range(len(text)):
            if text[i] in self._alphabet:
                diff = (self._alphabet.find(text[i]) 
                    - (self._alphabet.find(self._pass[i])))
                if diff < 0:
                    diff += len(self._alphabet)
                self._deciphered += self._alphabet[diff]
            else:
                self._deciphered += text[i]

        return self._deciphered


abc = "abcdefghijklmnopqrstuvwxyz"
key = "pizza"
c = VigenereCipher(key, abc)

print(c.encode('asodavwt'))