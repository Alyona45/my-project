from rich import print as rich_print 

name = input()

def change_name(name):
    new = []
    for index, letter in enumerate(name):
        if index % 2 == 0:
            new.append(letter.upper())
        else:
            new.append(letter.lower())
    return ''.join(new)

print(change_name(name))

def greet(name):
    rich_print(f'Hello, [bold blue]{change_name(name)}[/bold blue]!')

print(greet(name))


