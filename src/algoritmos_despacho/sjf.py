from heapq import heappush, heappop

from algoritmos_despacho.process import Process

def sjf(processes: list[Process]):
  '''
  Shortest Job First (SJF) scheduling algorithm.

  This function takes a list of processes and schedules them using the SJF algorithm.
  The processes are sorted based on their arrival time, and then processed in the order of their burst time.
  The function returns a queue of processes in the order they are scheduled.

  Args:
    processes (list[Process]): A list of Process objects representing the processes to be scheduled.

  Returns:
    list[tuple]: A queue of processes in the order they are scheduled. 
    Each element in the queue is a tuple 
    containing the arrival time, process ID, and the Process object.
  '''
  sorted_processes = sorted(processes, key=lambda x: x.arrival_time)
  queue = []
  
  count_time = 0
  
  temp_queue = []
  
  while sorted_processes or temp_queue:
  
    while sorted_processes and sorted_processes[0].arrival_time <= count_time:
      process = sorted_processes.pop(0)
      heappush(temp_queue, (process.burst_time, process.id, process))
    
    if temp_queue:
      process = heappop(temp_queue)[-1]
      process.waiting_time = count_time - process.arrival_time
      process.system_time = process.waiting_time + process.burst_time
      heappush(queue, (process.arrival_time, process.id, process))
      count_time += process.burst_time
  
  return queue