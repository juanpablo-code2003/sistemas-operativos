import matplotlib.pyplot as plt

def create_gantt(title, entries):
  fig, ax = plt.subplots()
  start_time = 0

  ax.set_ylim(0, len(entries)-1)

  # Obtain data from entries
  total_time = 0
  txt = ''
  ylabels = []
  for entry in entries:
    if entry[1] == -1:
      txt += f'Average waiting time: {entry[-1][0]}      Average system time: {entry[-1][1]}\n'
      continue
    total_time += entry[-1].burst_time
    ylabels.append(entry[-1].id)
    txt += f'{entry[-1]}\n'


  #total_time = sum(entry[-1].burst_time for entry in entries)
  ax.set_xlim(0, total_time)

  # Plot the horizontal bars with different colors
  colors = ['blue', 'green', 'red', 'orange', 'purple', 'brown']
  for i, entry in enumerate(entries):
    if entry[1] != -1:
      ax.broken_barh([(start_time, entry[-1].burst_time)], (i, 1), facecolors=colors[i % len(colors)])
      start_time += entry[-1].burst_time

  ax.set_title(title)

  ax.set_yticks(range(len(entries)-1))
  # ax.set_yticklabels([entry[-1].id for entry in entries])
  ax.set_yticklabels(ylabels)

  ax.set_xlabel('Time(s)')
  #txt = "\n".join([f'{entry[-1]}' for entry in entries])
  ax.text(0, -0.2, txt, transform=ax.transAxes, verticalalignment='top', fontsize=10)

  # Adjust the layout to display the text
  plt.tight_layout()

  # Show the plot
  plt.show()
