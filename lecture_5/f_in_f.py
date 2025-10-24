def print_to_console(init_value: int):
    print(init_value)
    print('Hello')
    
print_to_console(2)

def no_return(value: int) -> int:
    if value % 2 == 0:
        value *= 10
        if value == 20:
            return
        
y = 0

def after_return() -> int:
    global y
    return y * 10
    print('hey')
    
def rec(x: int) -> int:
    print(x)
    x += 1
    if x < 100:
        rec(x)
        
    return x
    
print(
    after_return
)

rec(0)
