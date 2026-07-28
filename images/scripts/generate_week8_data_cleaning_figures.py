import os
import numpy as np

# Set MPLCONFIGDIR before importing matplotlib
os.environ['MPLCONFIGDIR'] = '/tmp'

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.rcParams['font.size'] = 10

# Output images directly to the parent images directory
script_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.abspath(os.path.join(script_dir, ".."))
os.makedirs(output_dir, exist_ok=True)

# ---------------------------------------------------------
# Figure 1: Boxplot & Outlier Fences
# ---------------------------------------------------------
fig, (ax_dist, ax_box) = plt.subplots(2, 1, figsize=(10, 6), sharex=True, gridspec_kw={'height_ratios': [1.2, 1]})

mu, sigma = 0, 1
x = np.linspace(-4.5, 4.5, 1000)
y = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma)**2)

# Normal curve
ax_dist.plot(x, y, color='#2b5c8f', lw=2, label='Normal Distribution')
ax_dist.fill_between(x, y, color='#2b5c8f', alpha=0.15)
ax_dist.set_ylabel('Probability Density', fontsize=11, fontweight='bold')
ax_dist.set_title('Univariate Outlier Fences & Boxplot Alignment', fontsize=14, fontweight='bold', pad=12)

# Quartiles and Fences for N(0,1)
q1 = -0.6745
q2 = 0.0
q3 = 0.6745
iqr = q3 - q1
inner_low = q1 - 1.5 * iqr
inner_high = q3 + 1.5 * iqr

for fence, col in [(inner_low, '#e66101'), (inner_high, '#e66101')]:
    if -4.5 <= fence <= 4.5:
        ax_dist.axvline(fence, color=col, linestyle='--', alpha=0.8, lw=1.5)

# Boxplot
box_props = dict(patch_artist=True, boxprops=dict(facecolor='#a6cee3', color='#1f78b4', lw=2),
                 whiskerprops=dict(color='#1f78b4', lw=2),
                 capprops=dict(color='#1f78b4', lw=2),
                 medianprops=dict(color='#b2182b', lw=2.5))

np.random.seed(42)
data = np.random.normal(0, 1, 300)
data = np.append(data, [2.85, 3.4, -2.9])

ax_box.boxplot(data, vert=False, positions=[0.5], widths=0.4, **box_props)
ax_box.set_yticks([])
ax_box.set_xlabel('Value (Standardised)', fontsize=11, fontweight='bold')

ax_box.annotate(r'$Q_1$', xy=(q1, 0.7), xytext=(q1-0.1, 0.85), fontweight='bold', fontsize=11, color='#1f78b4')
ax_box.annotate(r'$Q_2$ (Median)', xy=(q2, 0.7), xytext=(q2-0.3, 0.85), fontweight='bold', fontsize=11, color='#b2182b')
ax_box.annotate(r'$Q_3$', xy=(q3, 0.7), xytext=(q3-0.1, 0.85), fontweight='bold', fontsize=11, color='#1f78b4')

ax_box.annotate('', xy=(q1, 0.25), xytext=(q3, 0.25), arrowprops=dict(arrowstyle='<->', color='#1f78b4', lw=2))
ax_box.text(0, 0.15, 'IQR', ha='center', va='center', fontweight='bold', fontsize=11, color='#1f78b4')

ax_box.axvline(inner_high, color='#e66101', linestyle='--', lw=1.5)
ax_box.axvline(inner_low, color='#e66101', linestyle='--', lw=1.5)
ax_box.text(inner_high + 0.1, 0.5, 'Mild Outliers\n(Beyond 1.5 IQR)', color='#e66101', fontsize=9, fontweight='bold', va='center')

plt.tight_layout()
fig.savefig(os.path.join(output_dir, 'boxplot_fences.png'), dpi=300)
plt.close(fig)


# ---------------------------------------------------------
# Figure 2: Masking & Swamping
# ---------------------------------------------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

np.random.seed(10)
normal_pts = np.random.normal(10, 1, 25)

# Masking
masking_pts = np.append(normal_pts, [22, 23])
ax1.scatter(range(len(normal_pts)), normal_pts, color='#2b5c8f', label='Normal Data', s=40)
ax1.scatter([25, 26], [22, 23], color='#d95f02', s=70, label='Outliers (Pair)', zorder=5)
ax1.axhline(np.mean(masking_pts), color='#7570b3', linestyle=':', lw=2, label=f'Mean (Skewed = {np.mean(masking_pts):.1f})')
ax1.set_title('A. Masking Effect', fontsize=13, fontweight='bold')
ax1.set_ylabel('Observation Value', fontsize=11)
ax1.set_xlabel('Observation Index', fontsize=11)
ax1.annotate('Outlier 1 inflates variance,\nmasking Outlier 2 from single-test', xy=(25, 22), xytext=(8, 19),
             arrowprops=dict(facecolor='#d95f02', shrink=0.05, width=1.5, headwidth=8), fontsize=9, fontweight='bold')
ax1.legend(loc='upper left', frameon=True)

# Swamping
swamping_pts = np.append(normal_pts, [25, 26, 27, 28])
ax2.scatter(range(len(normal_pts)), normal_pts, color='#2b5c8f', label='Normal Data', s=40)
ax2.scatter([25, 26, 27, 28], [25, 26, 27, 28], color='#d95f02', s=70, label='Outlier Cluster', zorder=5)
low_normal_idx = int(np.argmin(normal_pts))
ax2.scatter(low_normal_idx, normal_pts[low_normal_idx], color='#e7298a', s=80, marker='s', label='Swamped Normal Point', zorder=5)
ax2.set_title('B. Swamping Effect', fontsize=13, fontweight='bold')
ax2.set_xlabel('Observation Index', fontsize=11)
ax2.annotate('Cluster shifts mean & variance;\nnormal point flagged as false outlier', xy=(low_normal_idx, normal_pts[low_normal_idx]), xytext=(2, 4),
             arrowprops=dict(facecolor='#e7298a', shrink=0.05, width=1.5, headwidth=8), fontsize=9, fontweight='bold')
ax2.legend(loc='upper left', frameon=True)

plt.tight_layout()
fig.savefig(os.path.join(output_dir, 'masking_swamping.png'), dpi=300)
plt.close(fig)


# ---------------------------------------------------------
# Figure 3: Missing Data Mechanisms (MCAR, MAR, MNAR)
# ---------------------------------------------------------
fig, axes = plt.subplots(1, 3, figsize=(14, 4.5))

np.random.seed(42)
n_rows = 12

age = np.random.randint(20, 70, n_rows)
income = age * 1.5 + np.random.normal(0, 10, n_rows) + 30

def draw_matrix(ax, missing_mask, title, subtitle):
    grid = np.zeros((n_rows, 2))
    grid[:, 1] = missing_mask.astype(int)
    
    img_data = np.zeros((n_rows, 2, 3))
    for r in range(n_rows):
        for c in range(2):
            if grid[r, c] == 0:
                img_data[r, c] = [0.168, 0.361, 0.561] # #2b5c8f
            else:
                img_data[r, c] = [0.902, 0.380, 0.004] # #e66101
                
    ax.imshow(img_data, aspect='auto')
    ax.set_xticks([0, 1])
    ax.set_xticklabels(['Age (Observed)', 'Income (Target)'], fontweight='bold', fontsize=10)
    ax.set_ylabel('Subject Index', fontweight='bold', fontsize=10)
    ax.set_title(title, fontsize=12, fontweight='bold', pad=10)
    ax.text(0.5, -0.15, subtitle, transform=ax.transAxes, ha='center', fontsize=9, style='italic')
    
    ax.set_xticks(np.arange(-.5, 2, 1), minor=True)
    ax.set_yticks(np.arange(-.5, n_rows, 1), minor=True)
    ax.grid(which='minor', color='white', linestyle='-', linewidth=2)
    ax.tick_params(which='minor', size=0)

mcar_mask = np.random.choice([False, True], size=n_rows, p=[0.7, 0.3])
draw_matrix(axes[0], mcar_mask, '1. MCAR (Completely at Random)', 'Missingness is independent of data')

mar_mask = age > 48
draw_matrix(axes[1], mar_mask, '2. MAR (At Random)', 'Missingness depends on observed Age')

mnar_mask = income > np.percentile(income, 65)
draw_matrix(axes[2], mnar_mask, '3. MNAR (Not at Random)', 'Missingness depends on unobserved Income')

plt.tight_layout()
fig.savefig(os.path.join(output_dir, 'missing_data_mechanisms.png'), dpi=300)
plt.close(fig)


# ---------------------------------------------------------
# Figure 4: Moving Average Smoothing & Trade-offs
# ---------------------------------------------------------
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 7), sharex=True)

np.random.seed(15)
t = np.linspace(0, 50, 200)
true_signal = np.sin(t / 4) * 10 + t * 0.2
noise = np.random.normal(0, 2.5, len(t))
raw_signal = true_signal + noise

def sma(arr, n, centered=False):
    res = np.empty_like(arr)
    res[:] = np.nan
    if not centered:
        for i in range(n-1, len(arr)):
            res[i] = np.mean(arr[i-n+1:i+1])
    else:
        half = n // 2
        for i in range(half, len(arr) - half):
            res[i] = np.mean(arr[i-half:i+half+1])
    return res

ax1.plot(t, raw_signal, color='gray', alpha=0.4, label='Raw Noisy Signal', lw=1)
ax1.plot(t, sma(raw_signal, 3), color='#1b9e77', lw=1.8, label='Small Window (n=3): High Noise, High Responsiveness')
ax1.plot(t, sma(raw_signal, 25), color='#d95f02', lw=2.2, label='Large Window (n=25): Smooth, but Flattens Peaks & Lags')
ax1.set_ylabel('Signal Value', fontsize=11, fontweight='bold')
ax1.set_title('A. Impact of Moving Average Window Size (n)', fontsize=13, fontweight='bold')
ax1.legend(loc='upper left', frameon=True)

ax2.plot(t, true_signal, color='black', linestyle='--', lw=1.5, label='True Signal (No Noise)')
ax2.plot(t, sma(raw_signal, 15, centered=False), color='#7570b3', lw=2, label='One-Sided SMA (n=15): Real-time (Phase Lag Shifted Right)')
ax2.plot(t, sma(raw_signal, 15, centered=True), color='#e7298a', lw=2, label='Two-Sided Centred SMA (n=15): Offline (No Phase Lag)')
ax2.set_ylabel('Signal Value', fontsize=11, fontweight='bold')
ax2.set_xlabel('Time / Observation Index', fontsize=11, fontweight='bold')
ax2.set_title('B. One-Sided (Phase Lag) vs. Two-Sided (Centred) Moving Average', fontsize=13, fontweight='bold')
ax2.legend(loc='upper left', frameon=True)

plt.tight_layout()
fig.savefig(os.path.join(output_dir, 'moving_average_smoothing.png'), dpi=300)
plt.close(fig)

print("All 4 figures generated successfully in:", output_dir)
