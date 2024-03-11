from heapq import heappush, heappop

from algoritmos_despacho.process import Process

def priority(processes: list[Process]):
  """
  Priority scheduling algorithm implementation.

  Args:
    processes (list[Process]): A list of Process objects representing the processes to be scheduled.

  Returns:
    list[tuple]: A list of tuples representing the scheduled processes in the order of their execution.
      Each tuple contains the arrival time, process ID, and the Process object itself.

  """
  sorted_processes = sorted(processes, key=lambda x: x.arrival_time)
  queue = []
  count_time = 0
  average_waiting_time = 0
  average_system_time = 0
  temp_queue = []

  while sorted_processes or temp_queue:
    while sorted_processes and sorted_processes[0].arrival_time <= count_time:
      process = sorted_processes.pop(0)
      heappush(temp_queue, (process.priority, process.id, process))

    if temp_queue:
      process = heappop(temp_queue)[-1]
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