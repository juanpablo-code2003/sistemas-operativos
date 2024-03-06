class Process:
  def __init__(self, id, arrival_time, burst_time):
    self.id = id
    self.arrival_time = arrival_time
    self.burst_time = burst_time
    
  def __str__(self):
    return f'Process {self.id} (arrival_time: {self.arrival_time}, burst_time: {self.burst_time})'