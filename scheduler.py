import _process
import _queue

# number of processes
num_processes = 0
# a list of processes
pool = [
    _process.Process("P1", 4, 1),
    _process.Process("P2", 2, 2),
    _process.Process("P3", 5, 3),
    _process.Process("P4", 5, 4),
]

def init():
    # get the number of processes from the user
    global num_processes
    num_processes = int(input("Enter number of processes: "))

    # create processes and store in the processes pool
    for i in range(num_processes):
        p = _process.create("P" + str(i))
        
        # store the created process in the pool
        pool.append(p)

    _queue.init(pool)


# start the app
init()