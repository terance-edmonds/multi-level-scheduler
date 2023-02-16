import time
from rich.console import Console
from rich.progress import Progress
from rich.table import Table

console = Console()

# process structure
class Process:
    burst = 0.0
    queue = 1
    def __init__(self, name, burst, queue):
        self.name = name
        self.burst = burst
        self.queue = queue

# get process details from the user and return a process object
def create(name):
    burst = float(input("Enter process burst time (seconds): "))
    queue = int(input("Enter process queue: "))

    # check if the queue number is valid
    if(queue < 0 and queue > 4):
        print("queue is not available, Queues - (1, 2, 3, 4)")

    # create a process return it
    return Process(name, burst, queue)

# run a process
def run1(seconds, process):
    with console.status(f"[bold green]Working on process [bold red]{process.name}...") as status:
        t_end = time.time() + seconds
        
        while time.time() < t_end:
            process

    return 1

def run(seconds, process):
    t_sleep = 0.1

    with Progress() as progress:
        task = progress.add_task(f"[red]Processing {process.name}...", total=seconds)

        while not progress.finished:
            progress.update(task, advance=t_sleep)
            time.sleep(t_sleep)
    
    process.burst -= seconds
    if(process.burst == 0):
        return 1 # process completed
    
    return 0 # process on going

# display process status
def display(p, _time, queue_no):
    queue_names = {
        1: "round robin",
        2: "shortest job first",
        3: "shortest job first",
        4: "first come first serve",
    }
    status = "on going"

    if(p.burst == 0):
        status = "completed"

    table = Table()

    table.add_column("Attribute", style="cyan", no_wrap=True, min_width=15)
    table.add_column("Value", justify="right", style="green", min_width=25)

    table.add_row("name", f"{p.name}")
    table.add_row("burst time (s)", f"{p.burst}")
    table.add_row("scheduler", f"{queue_names[queue_no]}")
    table.add_row("state", status)
    table.add_row("last process duration (s)", f"{_time}")
    
    console.log(f"{p.name} process status")
    console.print(table)