from algoritmos_despacho.fifo import fifo
from algoritmos_despacho.process import Process

if __name__ == '__main__':
  processes = [
    Process(1, 0, 10),
    Process(2, 0, 5),
    Process(3, 2, 8),
    Process(4, 3, 4),
    Process(5, 3, 6)
  ]
  
  for queue in fifo(processes):
    print(queue[2])