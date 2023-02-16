# <img src="https://media.giphy.com/media/njLmVHGPuflqSb5hfb/giphy.gif" width="50" heigh="50" /> Multilevel Queue Scheduling

A program to simulate a multilevel queue scheduling algorithm with 4 queues. Each queue
must be assigned a priority, with q0 having the highest priority and q3 having the lowest priority.

The following scheduling algorithms are used for each queue:

```
    ● q0 - Round Robin (RR)
    ● q1 - Shortest Job First (SJF)
    ● q2 - Shortest Job First (SJF)
    ● q3 - First-In-First-Out (FIFO)
````

Each queue should be given a time quantum of 20 seconds, and the CPU should switch
between queues after every 20 seconds. The user should be prompted to enter the number of
processes along with their priority associated with each queue.