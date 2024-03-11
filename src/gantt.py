import matplotlib.pyplot as plt

def create_gantt(entries):
  fig, ax = plt.subplots()
  start_time = 0

  ax.set_ylim(0, len(entries))

  total_time = sum(entry[-1].burst_time for entry in entries)
  ax.set_xlim(0, total_time)

  # Plot the horizontal bars with different colors
  colors = ['blue', 'green', 'red', 'orange', 'purple', 'brown']
  for i, entry in enumerate(entries):
    ax.broken_barh([(start_time, entry[-1].burst_time)], (i, 1), facecolors=colors[i % len(colors)])
    start_time += entry[-1].burst_time

  # Set the y-axis labels
  ax.set_yticks(range(len(entries)))
  ax.set_yticklabels([entry[-1].id for entry in entries])

  # Set the x-axis label
  ax.set_xlabel('Time', ha='center')

  # Show the plot
  plt.show()
