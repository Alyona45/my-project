class HumanInLaw:
    
    def __init__(
        self,
        name: str = "Vova",
        legs: int = 2,
        eyes: int = 2,
        hands: int = 2,
        hair: str = 'brown'
    ):
        self.name = name
        self.legs = legs
        self.eyes = eyes
        self.hands = hands
        self.hair = hair
    
    def blink(self):
        print(f"{self.name} blinked with {self.eyes}")
        
    def walk(self):
        print(f"{self.name} walked away")
        
    def break_plank(self, plank_material: str = "wooden", quantity: int = 2):
        print(
            f"{self.name} breaks {quantity} {plank_material} plank"
        )
class SmartHuman(HumanInLaw):
    glasses: bool = True
    IQ: int = 130
    
    def __init__(self, glasses: bool = True, IQ: int = 130):
        super().__init__() #вызов инита родителя
        self.glasses = glasses
        self.IQ = IQ
        
    def blink(self):
        print(
            f"Smart {self.name} blinked with {self.eyes} eyes "
            f"and with glasses {"on" if self.glasses is True else 'off'}"
        )
if __name__ == '__main__':
    human1 = HumanInLaw()
    
    human1.blink()
    human1.break_plank()
    human1.break_plank("plastic", 3)
    
    human2 = HumanInLaw(name="Andrey", legs=2)
    human2.blink()
    
    smart_human1 = SmartHuman()
    smart_human1.blink()