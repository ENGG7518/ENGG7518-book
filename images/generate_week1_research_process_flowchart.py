"""
Script: generate_week1_research_process_flowchart.py
Target Output: quarto_files/images/research-process.png
Used In: quarto_files/fundamentals/week1_what-is-science.qmd (#fig-research-process)
Description: Generates the 7-node circular flowchart with 'THEORY' at the center, matching Slide 24 of Lecture 1 (arrows 1->2->...->7, no 7->1 arrow).
"""

import os
import matplotlib.pyplot as plt
import numpy as np

# Script location & output target setup
script_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(script_dir, "research-process.png")

# Tight figure size matching exact content aspect ratio (span_x = 3.3, span_y = 2.6 -> 1.27 ratio)
fig, ax = plt.subplots(figsize=(6.5, 5.12), dpi=300)
ax.set_aspect('equal')
ax.axis('off')

# Center node: THEORY
center_x, center_y = 0, 0
circle_center = plt.Circle((center_x, center_y), 0.32, color='#4B2E83', ec='#2E1A47', lw=2, zorder=5)
ax.add_patch(circle_center)
ax.text(center_x, center_y, "THEORY", color='white', weight='bold', fontsize=11, ha='center', va='center', zorder=6)

# 7 Outer nodes matching Lecture 1 Slide 24
labels = [
    "1. Select Topic",
    "2. Focus Question",
    "3. Design Study",
    "4. Collect Data",
    "5. Analyze Data",
    "6. Interpret Data",
    "7. Inform Others"
]

num_nodes = 7
radius = 1.15

# Angles in radians (starting top = pi/2, clockwise)
angles = [np.pi/2 - i * (2 * np.pi / num_nodes) for i in range(num_nodes)]

coords = []
for i, angle in enumerate(angles):
    x = radius * np.cos(angle)
    y = radius * np.sin(angle)
    coords.append((x, y))
    
    # Draw node box
    bbox_props = dict(boxstyle="round,pad=0.35", fc="#F8F9FA", ec="#4B2E83", lw=1.6)
    ax.text(x, y, labels[i], color="#1D2A44", weight="bold", fontsize=9.5, ha="center", va="center", bbox=bbox_props, zorder=5)

    # Draw dashed line from THEORY to outer node
    ax.annotate("", xy=(x * 0.72, y * 0.72), xytext=(center_x, center_y),
                arrowprops=dict(arrowstyle="->", color="#708090", ls="--", lw=1.2), zorder=3)

# Draw forward arrows between consecutive outer nodes (from 1->2 up to 6->7, excluding 7->1)
for i in range(num_nodes - 1):
    x1, y1 = coords[i]
    x2, y2 = coords[i + 1]
    
    dx, dy = x2 - x1, y2 - y1
    dist = np.hypot(dx, dy)
    ux, uy = dx / dist, dy / dist
    
    start_x, start_y = x1 + ux * 0.38, y1 + uy * 0.38
    end_x, end_y = x2 - ux * 0.38, y2 - uy * 0.38
    
    ax.annotate("", xy=(end_x, end_y), xytext=(start_x, start_y),
                arrowprops=dict(arrowstyle="-|>", color="#4B2E83", lw=1.5, mutation_scale=11), zorder=4)

# Tight x and y limits fitting content without extra vertical padding
plt.xlim(-1.62, 1.62)
plt.ylim(-1.22, 1.35)

plt.savefig(output_path, dpi=300, bbox_inches='tight', pad_inches=0.02)
print(f"Successfully generated flowchart: {output_path}")
