from heapq import heappush

from algoritmos_despacho.process import Process

def fifo(processes: list[Process]):
  '''
  First-In, First-Out (FIFO) algorithm for process scheduling.

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
  average_waiting_time = 0
  average_system_time = 0
  
  for process in sorted_processes:
    process.waiting_time = count_time - process.arrival_time
    process.system_time = process.waiting_time + process.burst_time
    heappush(queue, (process.arrival_time, process.id, process))
    count_time += process.burst_time
    average_waiting_time += process.waiting_time
    average_system_time += process.system_time

  average_waiting_time /= len(processes)
  average_system_time /= len(processes)
  heappush(queue, (count_time, -1, [average_waiting_time, average_system_time]))
  
  return queue