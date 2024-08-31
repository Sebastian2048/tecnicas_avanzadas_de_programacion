from matplotlib {} import pyplot as plt
from  matplotlib {} import patches as mpatches

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Define positions for the boxes
os_box = [0.1, 0.7, 0.8, 0.2]
open_cpn_box = [0.2, 0.75, 0.6, 0.1]
moxa_box = [0.1, 0.4, 0.3, 0.2]
sensors_box = [0.1, 0.2, 0.3, 0.1]
communication_box = [0.6, 0.4, 0.3, 0.2]
network_box = [0.6, 0.3, 0.3, 0.1]

# Add the boxes to the plot
ax.add_patch(mpatches.FancyBboxPatch((os_box[0], os_box[1]), os_box[2], os_box[3],
                                     boxstyle="round,pad=0.05", edgecolor="black", facecolor="lightgray"))
ax.text(0.5, 0.82, "General Purpose OS\n(Linux/Windows/macOS)", ha='center', va='center', fontsize=12)

ax.add_patch(mpatches.FancyBboxPatch((open_cpn_box[0], open_cpn_box[1]), open_cpn_box[2], open_cpn_box[3],
                                     boxstyle="round,pad=0.05", edgecolor="black", facecolor="lightblue"))
ax.text(0.5, 0.80, "OpenCPN", ha='center', va='center', fontsize=12)

ax.add_patch(mpatches.FancyBboxPatch((moxa_box[0], moxa_box[1]), moxa_box[2], moxa_box[3],
                                     boxstyle="round,pad=0.05", edgecolor="black", facecolor="lightgray"))
ax.text(0.25, 0.48, "Moxa Device\n(Microcontroller)", ha='center', va='center', fontsize=12)

ax.add_patch(mpatches.FancyBboxPatch((sensors_box[0], sensors_box[1]), sensors_box[2], sensors_box[3],
                                     boxstyle="round,pad=0.05", edgecolor="black", facecolor="lightgreen"))
ax.text(0.25, 0.25, "Sensors", ha='center', va='center', fontsize=12)

ax.add_patch(mpatches.FancyBboxPatch((communication_box[0], communication_box[1]), communication_box[2], communication_box[3],
                                     boxstyle="round,pad=0.05", edgecolor="black", facecolor="lightgray"))
ax.text(0.75, 0.48, "Communication\nInterface", ha='center', va='center', fontsize=12)

ax.add_patch(mpatches.FancyBboxPatch((network_box[0], network_box[1]), network_box[2], network_box[3],
                                     boxstyle="round,pad=0.05", edgecolor="black", facecolor="lightyellow"))
ax.text(0.75, 0.35, "Network", ha='center', va='center', fontsize=12)

# Draw arrows
arrowprops = dict(facecolor='black', arrowstyle="->")

ax.annotate('', xy=(0.5, 0.7), xytext=(0.75, 0.6), arrowprops=arrowprops)
ax.annotate('', xy=(0.4, 0.7), xytext=(0.3, 0.6), arrowprops=arrowprops)
ax.annotate('', xy=(0.25, 0.4), xytext=(0.25, 0.3), arrowprops=arrowprops)
ax.annotate('', xy=(0.75, 0.4), xytext=(0.75, 0.3), arrowprops=arrowprops)
ax.annotate('', xy=(0.45, 0.4), xytext=(0.55, 0.4), arrowprops=arrowprops)

# Set limits and title
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')
ax.set_title("Integration of OpenCPN with Moxa Device and Sensors", fontsize=14)

# Show the plot
plt.show()
