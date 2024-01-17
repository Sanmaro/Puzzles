class VersionManager:
    def __init__(self, version="0.0.1"):
        try:
            self._version_temp = [int(ver) for ver in version.split(".")[:3]]
            self._version_temp.extend([0, 0])
            self._version = [tuple(self._version_temp)]
        except ValueError:
            if version == "":
                self._version = [(0, 0, 1)]
            else:
                raise ValueError("Error occured while parsing version!")
  
        
    def major(self):
        self._version.append((
            self._version[-1][0] + 1,
            0, 
            0))
        return self

    def minor(self):
        self._version.append((
            self._version[-1][0], 
            self._version[-1][1] + 1, 
            0))
        return self
    
    def patch(self):
        self._version.append((
            self._version[-1][0], 
            self._version[-1][1], 
            self._version[-1][2] + 1))
        return self
    
    def rollback(self):
        if len(self._version) > 1:
            self._version.pop()
            return self
        elif len(self._version) <= 1:
            raise IndexError("Cannot rollback!")
        return self
        
    def release(self):
        return ".".join(map(str, self._version[-1][:3]))


print(VersionManager().rollback().release())
