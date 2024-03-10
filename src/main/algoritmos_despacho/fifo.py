from heapq import heappush

from algoritmos_despacho.process import Process

def fifo(processes: list[Process]):
  
  queue = []
  
  for i, process in enumerate(processes):
    heappush(queue, (process.arrival_time, i, process))
  
  return queue