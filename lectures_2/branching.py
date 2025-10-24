from rich import print as rich_print

rich_print('[bold blue]Привет, мой друг!')
rich_print('Сегодня у нас будет показ фильма [bold red]Дедпул[/bold red]')
decision = input('Пойдешь со мной?: [Да\Нет]')
decision = decision.capitalize()

#decision.upper()
#decision.lower()

if decision == 'Да':
    age_18 = input('А тебе есть 18?')
    if age_18.lower == 'да' or int(age_18) >= 18:
        print('Тогда в 19ч у кинотеатра, не опаздывай!')
    else:
        print('Тебя не пустят')
else:
    print('Ну как хочешь :(')
    

    
