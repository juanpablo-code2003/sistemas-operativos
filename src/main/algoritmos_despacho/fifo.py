from heapq import heappush

from algoritmos_despacho.process import Process

def fifo(processes: list[Process]):
  
  queue = []
  cont = 0
  
  for i, process in enumerate(processes):
    process.waiting_time = cont - process.arrival_time
    process.system_time = process.waiting_time + process.burst_time
    heappush(queue, (process.arrival_time, i, process))
    cont += process.burst_time
  
  return queue