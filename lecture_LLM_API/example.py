import dotenv
from openai import OpenAI
from settings import OpenAISettings
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown

dotenv.load_dotenv(dotenv.find_dotenv())

console = Console()

def get_client() -> OpenAI:
    settings = OpenAISettings()
    client = OpenAI(
        api_key=settings.openai_api_key.get_secret_value(),
        base_url=str(settings.openai_base_url),
    )
    return client

def chat_loop():
    client = get_client()
    messages = [
        {
            "role": "system",
            "content": "Ты русский православный батюшка матершинник, который составляет молитвы людям с кучей мата и эмодзи",
        }
    ]
    
    console.print(Panel(
        "[bold cyan]Оставь надежду, всяк сюда входящий![/bold cyan]\n\n"
        "Команды:\n"
        "  [yellow]/exit[/yellow] - выход из чата\n"
        "  [yellow]/clear[/yellow] - очистить историю\n"
        "  [yellow]/system <текст>[/yellow] - задать системный промпт",
        title="Позови меня тихо по имени",
        border_style="cyan"
    ))
    
    while True:
        
        user_input = console.input("\n[bold green]Вы:[/bold green] ")
        
        if user_input.strip() == "":
            continue
        
        if user_input.strip() == "/exit":
            console.print(Panel("[yellow]Перекрестись![/yellow]", border_style="yellow"))
            break
        
        elif user_input.strip() == "/clear":
            system_prompt = messages[0]
            messages = [system_prompt]
            console.print(Panel("[green]Отпускаю тебе все грехи![/green]", border_style="green"))
            continue
        
        elif user_input.strip().startswith("/system"):
            system_prompt = user_input[8:].strip()
            messages[0] = {
                "role": "system",
                "content": system_prompt
            }
            console.print(Panel(
                f"[green]Системный промпт обновлен:[/green]\n{system_prompt}",
                border_style="green"
            ))
        
        messages.append({
            "role": "user",
            "content": user_input
        })
        
        with console.status("[bold cyan]Думаю...[/bold cyan]", spinner="dots"):

            completion = client.chat.completions.create(
                model="Qwen/Qwen3-Next-80B-A3B-Instruct",
                messages=messages,
            )
                
            assistant_message = completion.choices[0].message.content
                
            messages.append({
                "role": "assistant",
                "content": assistant_message
            })
                
            md = Markdown(assistant_message)
            console.print(Panel(
                md,
                title="[bold blue]Батюшка:[/bold blue]",
                border_style="blue",
                padding=(1, 2)
            ))

if __name__ == "__main__":
    chat_loop()