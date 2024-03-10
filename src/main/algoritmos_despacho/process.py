class Process:
  def __init__(self, id: int, arrival_time: int, burst_time: int, priority: int = None):
    self.id = id
    self.arrival_time = arrival_time
    self.burst_time = burst_time
    self.priority = priority
    
  def __str__(self):
    return f'Process {self.id} (arrival_time: {self.arrival_time}, burst_time: {self.burst_time})'