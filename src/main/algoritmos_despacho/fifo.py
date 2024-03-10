from collections import deque

from algoritmos_despacho.process import Process

def fifo(processes: list[Process]):
  queue = deque(processes)
  
  while queue:
    process = queue.popleft()
    print(process)
  
  print('All processes have been executed')