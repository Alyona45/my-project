from abc import ABC, abstractmethod
from typing import override
class BaseDuck:
    wings: int = 2
    beak: bool = True
    
class MixInNoise():
    @abstractmethod
    @override
    def make_noise(self, volume_db: int) -> None:
        raise NotImplementedError

class MixInDustable():
    @abstractmethod
    def get_dusty(self) -> None:
        print('get dusty')
    
        
class Duckess(BaseDuck, MixInNoise, MixInDustable):
    def make_noise(self, volume_db: int) -> None:
        print(f"quackie ({volume_db: int} dB)")
        
class Duck(BaseDuck):
    
    def make_noise(self, volume_db: int) -> None:
        print(f"quack ({volume_db: int} dB)")
        
class BaseToy():
    material: str = 'plastic'
    
class ToyDuck (BaseDuck, BaseToy):
    def make_noise(self, volume_db: int) -> None:
        print(f"bzzz ({volume_db: int} dB)")
        
    
if __name__ == '__main__':
    d = Duck()
    d.make_noise()
    