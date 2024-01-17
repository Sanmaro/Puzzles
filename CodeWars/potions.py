class Potion:
    def __init__(self, color, volume):
        self.color = color
        self.volume = volume
    
    def mix(self, other):
        mixed = []
        ratio = self.volume / (self.volume + other.volume)
        for i in range(3):
            mixed.append((self.color[i] * ratio 
                          + other.color[i] * (1 - ratio)) 
                            / 2
                        )
        self.color = tuple(mixed)
        self.volume += other.volume
        return self
        
        
potions = [
    Potion((153, 210, 199), 32),
    Potion((135,  34,   0), 17),
    Potion((18,   19,  20), 25),
    Potion((174, 211,  13),  4),
    Potion((255,  23, 148), 19),
    Potion((51,  102,  51),  6)
]
a = potions[0].mix(potions[1])
b = potions[0].mix(potions[2]).mix(potions[4])
c = potions[1].mix(potions[2]).mix(potions[3]).mix(potions[5])

print(a.color, b.color, c.color)