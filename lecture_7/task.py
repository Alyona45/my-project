class MixInWalkable():
    def walk(self):
        print("Ну ноги в руки и пошли уже.")
        
class MixInJokable():
    def joke(self):
        print("Пошутить? А еще че сделать?")
        
class MixInSpeakable():
    def speak(self):
        print(f"Ну я {self.name}, что говорить...")
        
class MixInAnimatable():
    def animate(self):
        print(f"Ну я {self.name}, что делать?")
        
class MixInAnnoyed():
    def annoyed(self):
        print("ОСТАВЬТЕ МЕНЯ В ПОКОЕ!")
        
class MixInDancing():
    def dance(self):
        print(f"Да я {self.name} танцую!")
    
class MixInStaticable():
    def static(self):
        print(f"Ну я {self.name}, вытри с меня пыль!")
        
class MixInBeautiful():
    def beautiful(self):
        print(f"Я {self.name}, потратил много времени на костюм!")

class BaseHuman(MixInWalkable, MixInSpeakable):
    legs: int = 2
    arms: int = 2
    eyes: int = 2

class BaseCharacter(MixInSpeakable, MixInAnimatable):
    name: str
    
    def __init__(self, name):
        self.name = name
    
class BaseInActionCharacter(BaseCharacter, MixInWalkable):
    pass
    
class BaseFunkoPop(MixInStaticable):
    material: str = "plastic"
    
    def display(self):
        print("я пластиковая фигурка")
        
class BaseCosplayer(BaseHuman, BaseCharacter, MixInBeautiful):
    def __init__(self, name):
        BaseCharacter.__init__(self, name)
        self.cosplay_character = name

    def photo(self):
        print("Мне нужно сделать много фото, ведь я потратил на костюм деньги!")
    
class Shrek(BaseCharacter, MixInJokable, MixInAnnoyed):
    def __init__(self):
        super().__init__("Shrek")
        
class PussInBoots(BaseCharacter, MixInDancing):
    def __init__(self):
        super().__init__("Puss In Boots")

class Donkey(BaseCharacter, MixInJokable, MixInDancing):
    def __init__(self):
        super().__init__("Donkey")

class JackHorner(BaseCharacter, MixInJokable):
    def __init__(self):
        super().__init__("Jack Horner")
        

class ShrekInAction(Shrek, BaseInActionCharacter):
    pass

class PussInBootsInAction(PussInBoots, BaseInActionCharacter):
    pass

class DonkeyInAction(Donkey, BaseInActionCharacter):
    pass

class JackHornerInAction(JackHorner, BaseInActionCharacter):
    pass

class ShrekFunkoPop(Shrek, BaseFunkoPop):
    pass

class PussInBootsFunkoPop(PussInBoots, BaseFunkoPop):
    pass

class DonkeyFunkoPop(Donkey, BaseFunkoPop):
    pass

class JackHornerFunkoPop(JackHorner, BaseFunkoPop):
    pass

class ShrekCosplayer(BaseCosplayer):
    def __init__(self):
        super().__init__("Shrek Cosplayer")

class PussInBootsCosplayer(BaseCosplayer):
    def __init__(self):
        super().__init__("Puss In Boots Cosplayer")

class DonkeyCosplayer(BaseCosplayer):
    def __init__(self):
        super().__init__("Donkey Cosplayer")

class JackHornerCosplayer(BaseCosplayer):
    def __init__(self):
        super().__init__("Jack Horner Cosplayer")

if __name__ == "__main__":
    ch_1 = Shrek()
    ch_1.joke()
    ch_1.annoyed()
    
    ch_2 = Donkey()
    ch_2.dance()
    
    ch_3 = PussInBoots()
    ch_3.speak()
    
    ch_4 = JackHorner()
    ch_4.animate()

    
    funko_4 = JackHornerFunkoPop()
    funko_4.display()
    
    cosplayer_1 = ShrekCosplayer()
    cosplayer_1.photo()
    
    action_2 = PussInBootsInAction()
    action_2.walk()
    
    

