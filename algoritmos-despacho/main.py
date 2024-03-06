from fifo import fifo
from process import Process

if __name__ == '__main__':
  processes = [
    Process(1, 0, 10),
    Process(2, 1, 5),
    Process(3, 2, 8),
    Process(4, 3, 4),
    Process(5, 4, 6)
  ]
  
  fifo(processes)