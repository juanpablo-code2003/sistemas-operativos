from algoritmos_despacho.fifo import fifo
from algoritmos_despacho.sjf import sjf
from algoritmos_despacho.process import Process

if __name__ == '__main__':
  processes = [
    Process(0, 4),
    Process(1, 2),
    Process(2, 6),
    Process(3, 4),
  ]
  
  for queue in fifo(processes):
    print(queue[-1])