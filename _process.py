from rich.console import Console
from rich.table import Table

console = Console()

# simulate the current time
current_time = 0

# process structure
class Process:
    init_burst = 0
    burst = 0
    queue = 0
    arrival_time = 0
    complete_time = 0

    def __init__(self, id, burst, queue):
        self.id = id
        self.burst = burst
        self.queue = queue
        self.init_burst = burst
        self.arrival_time = current_time
        self.complete_time = 0

# get process details from the user and return a process object
def create(id):
    burst = float(input("Enter process burst time (seconds): "))
    queue = int(input("Enter process queue: "))

    # check if the queue number is valid
    if(queue < 0 or queue > 4):
        while (queue < 0 or queue > 4):
            print("queue is not available, Queues - (1, 2, 3, 4)")
            queue = int(input("Enter process queue: "))
    
    # create a process return it
    return Process(id, burst, queue)

# run a process
def run(_time, p):
    global current_time
    current_time += _time
    
    p.burst -= _time
    if(p.burst == 0):
        p.complete_time = current_time
        return 1 # process completed
    
    return 0 # process on going

# display process status
def display(p, _time, queue_no):
    queue_names = {
        0: "round robin",
        1: "shortest job first",
        2: "shortest job first",
        3: "first come first serve",
    }
    status = "on going"

    if(p.burst == 0):
        status = "completed"

    table = Table()

    table.add_column("Attribute", style="cyan", no_wrap=True, min_width=15)
    table.add_column("Value", justify="right", style="green", min_width=25)

    table.add_row("id", f"{p.id}")
    table.add_row("burst time (s)", f"{p.init_burst}")
    table.add_row("remaining burst time (s)", f"{p.burst}")
    table.add_row("scheduler", f"{queue_names[queue_no]}")
    table.add_row("state", status)
    table.add_row("last process duration (s)", f"{_time}")
    
    console.log(f"{p.id} process status")
    console.print(table)