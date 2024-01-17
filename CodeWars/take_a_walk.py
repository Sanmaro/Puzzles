class City:
    start = {"x": 0, "y": 0}
    position = {"x": 0, "y": 0}

    def is_valid_walk(self, walk):
        for direction in walk:
            match direction:
                case "n":
                    self.position["x"] -= 1
                case "e":
                    self.position["y"] += 1
                case "s":
                    self.position["x"] += 1
                case "w":
                    self.position["y"] -= 1
                case _:
                    pass
        if (self.position == self.start) and (len(walk) == 10):
            return True
        return False
    
city = City()
true_walk = ['n','s','n','s','n','s','n','s','n','s']
false_walk = ['w','e','w','e','w','e','w','e','w','e','w','e']
print(city.is_valid_walk(['n','n','n','s','n','s','n','s','n','s']))