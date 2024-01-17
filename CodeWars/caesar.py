class CaesarCipher(object):
    def __init__(self, shift):
        self.shift = shift

    def encode(self, st):
        encoded = [chr(ord(i) + self.shift - 26)
                   if ((ord(i) + self.shift) > ord("z")
                   and i.isalpha())
                   else chr(ord(i) + self.shift)
                   if i.isalpha()
                   else i 
                   for i in st.lower()]
        return "".join(map(str.upper, encoded))
        
    def decode(self, st):
        decoded = [chr(ord(i) - self.shift + 26) 
                   if ((ord(i) - self.shift) < ord("a")
                   and i.isalpha())
                   else chr(ord(i) - self.shift)
                   if i.isalpha()
                   else i 
                   for i in st.lower()]
        return "".join(map(str.upper, decoded))
    

c = CaesarCipher(5)
 
print(c.encode('Codewars it is'))
print(c.decode('HTIJBFWX " ypo ú'))