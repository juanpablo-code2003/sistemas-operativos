from algoritmos_despacho.fifo import fifo
from algoritmos_despacho.sjf import sjf
from algoritmos_despacho.process import Process
from algoritmos_despacho.priority import priority
from gantt import create_gantt

if __name__ == '__main__':
  processes = [
    Process(0, 4, 1),
    Process(1, 2, 2),
    Process(2, 6, 0),
    Process(3, 4, 2),
  ]
  
  print('\nFIFO')
  fifo_list = fifo(processes)
  for queue in fifo_list:
    print(queue[-1])
  create_gantt(fifo_list)

  print('\nSJF')
  sjf_list = sjf(processes)
  for queue in sjf_list:
    print(queue[-1])
  create_gantt(sjf_list)

  print('\nPriority')
  pri_list = priority(processes)
  for queue in pri_list:
    print(queue[-1])
  create_gantt(pri_list)