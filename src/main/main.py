from algoritmos_despacho.fifo import fifo
from algoritmos_despacho.sjf import sjf
from algoritmos_despacho.process import Process
from algoritmos_despacho.priority import priority

if __name__ == '__main__':
  processes = [
    Process(0, 4, 1),
    Process(1, 2, 2),
    Process(2, 6, 0),
    Process(3, 4, 2),
  ]
  
  for queue in priority(processes):
    print(queue[-1])