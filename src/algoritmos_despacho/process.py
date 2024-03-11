class Process:
  __idCount = 0
  
  def __init__(self, arrival_time: int, burst_time: int, priority: int = None):
    Process.__idCount += 1
    self.id = Process.__idCount
    self.arrival_time = arrival_time
    self.burst_time = burst_time
    self.priority = priority
    
    self.waiting_time = 0
    self.system_time = 0
    
  def __str__(self):
    priority = f' priority: {self.priority}' if self.priority is not None else ''
    return f'Process {self.id} (arrival_time: {self.arrival_time}, burst_time: {self.burst_time},{priority} waiting_time: {self.waiting_time}, system_time: {self.system_time})'