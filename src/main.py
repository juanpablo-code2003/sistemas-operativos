from algoritmos_despacho.fifo import fifo
from algoritmos_despacho.sjf import sjf
from algoritmos_despacho.process import Process
from algoritmos_despacho.priority import priority
from gantt import create_gantt
from csv import reader

if __name__ == '__main__':
  # Processes to be scheduled
  processes = []

  #Proposal of reading csv file with info about processes
  with open('pfile.csv', 'r') as csvfile:
    csvreader = reader(csvfile)
    for row in csvreader:
      processes.append(
        Process(int(row[0]), int(row[1]), int(row[2]))
      )

  #current implementation
  """
  processes = [
    Process(0, 4, 1),
    Process(1, 2, 2),
    Process(2, 6, 0),
    Process(3, 4, 2),
  ] """
  
  print('\nFIFO')
  fifo_list = fifo(processes)
  for queue in fifo_list:
    if (queue[1] == -1):
      print('Average waiting time:', queue[-1][0], 'Average system time:', queue[-1][1])
    else:
      print(queue[-1])
  create_gantt('FIFO', fifo_list)

  print('\nSJF')
  sjf_list = sjf(processes)
  for queue in sjf_list:
    if (queue[1] == -1):
      print('Average waiting time:', queue[-1][0], 'Average system time:', queue[-1][1])
    else:
      print(queue[-1])
  create_gantt('SJF', sjf_list)

  print('\nPriority')
  pri_list = priority(processes)
  for queue in pri_list:
    if (queue[1] == -1):
      print('Average waiting time:', queue[-1][0], 'Average system time:', queue[-1][1])
    else:
      print(queue[-1])
  create_gantt('Priority', pri_list)