import time
from functools import lru_cache

@lru_cache()

def calculate_greetings(name: str = 'Vova') -> str:
    wait_time: int = 5
    print(f'Waiting {wait_time} seconds...')
    time.sleep(wait_time)
    return f'Hello {name})'

MY_CACHE = dict[str, str] = {}
def calculate_surname(name: str = 'Vova'):
    wait_time = 5
    if name in MY_CACHE.keys():
        return MY_CACHE[name]
    surname = "Vova" + "4kin"
    MY_CACHE[name] = surname
    return surname

if __name__ == '__main__':
    _ = calculate_greetings(name ='Ilya')
    print(calculate_greetings('Andrey'))

print(F'{MY_CACHE=}')
_ = calculate_surname("Ilya")
_ = calculate_surname("Andrey")
