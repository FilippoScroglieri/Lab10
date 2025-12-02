from dataclasses import dataclass

@dataclass
class Tratta:
    hub1:str
    hub2:str
    peso:float

    def __str__(self):
        return f'{self.hub1} {self.hub2} {self.peso}'
    def __repr__(self):
        return f'{self.hub1} {self.hub2} {self.peso}'
    def __hash__(self):
        return hash((self.hub1, self.hub2, self.peso))