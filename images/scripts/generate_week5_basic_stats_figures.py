import os
import numpy as np

# Set MPLCONFIGDIR before importing matplotlib
os.environ['MPLCONFIGDIR'] = '/tmp'

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import scipy.stats as stats

plt.rcParams['font.size'] = 10
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'

script_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.abspath(os.path.join(script_dir, ".."))
os.makedirs(output_dir, exist_ok=True)

# ---------------------------------------------------------
# Figure 1: CI Interpretation - Repeated Sampling
# ---------------------------------------------------------
fig, ax = plt.subplots(figsize=(9, 6))

np.random.seed(42)
mu = 50
sigma = 10
n = 30
num_samples = 25

ax.axvline(mu, color='#b2182b', linestyle='--', lw=2, label=r'True Population Mean ($\mu = 50$)')

covers_count = 0
for i in range(1, num_samples + 1):
    sample = np.random.normal(mu, sigma, n)
    xbar = np.mean(sample)
    se = np.std(sample, ddof=1) / np.sqrt(n)
    margin = 2.045 * se # t_crit for df=29, 95%
    ci_low = xbar - margin
    ci_high = xbar + margin
    
    covers = (ci_low <= mu <= ci_high)
    if covers:
        covers_count += 1
        color = '#2b5c8f'
    else:
        color = '#e66101'
        
    ax.plot([ci_low, ci_high], [i, i], color=color, lw=1.8)
    ax.scatter(xbar, i, color=color, s=20)

ax.set_yticks(range(1, num_samples + 1))
ax.set_yticklabels([f'Sample {i}' for i in range(1, num_samples + 1)], fontsize=8)
ax.set_xlabel(r'Parameter Estimate & 95% Confidence Interval', fontweight='bold', fontsize=11)
ax.set_title(r'95% Confidence Intervals Across 25 Repeated Random Samples', fontweight='bold', fontsize=13, pad=12)
ax.legend(loc='upper right', frameon=True)
ax.text(0.02, 0.03, f'{covers_count}/25 Intervals capture true $\\mu$', transform=ax.transAxes, fontweight='bold', fontsize=10, bbox=dict(facecolor='white', alpha=0.8, edgecolor='gray'))

plt.tight_layout()
fig.savefig(os.path.join(output_dir, 'ci_repeated_sampling.png'), dpi=300)
plt.close(fig)

# ---------------------------------------------------------
# Figure 2: Traffic Counts Sample Data Dot Plot
# ---------------------------------------------------------
fig, ax = plt.subplots(figsize=(9, 3.5))

traffic = np.array([5224, 5480, 4960, 5368, 3860])
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
xbar = np.mean(traffic) # 4978.4
mu0 = 5000

ax.scatter(traffic, [1]*5, color='#2b5c8f', s=120, zorder=4, label='Daily Traffic Counts')
for t_val, day in zip(traffic, days):
    ax.annotate(f'{day}\n({t_val})', (t_val, 1), textcoords="offset points", xytext=(0, 15), ha='center', fontsize=9, fontweight='bold')

ax.axvline(mu0, color='#b2182b', linestyle='--', lw=2, label=r'Hypothesised Mean ($H_0: \mu_0 = 5000$)')
ax.scatter([xbar], [1], color='#e66101', marker='D', s=140, zorder=5, label=f'Sample Mean ($\\bar{{x}} = {xbar:.1f}$)')

ax.set_ylim(0.5, 1.6)
ax.set_yticks([])
ax.set_xlabel('Daily Traffic Volume (vehicles/day)', fontweight='bold', fontsize=11)
ax.set_title('St Lucia Campus Daily Traffic Sample Data ($n=5$)', fontweight='bold', fontsize=13, pad=12)
ax.legend(loc='upper left', frameon=True)

plt.tight_layout()
fig.savefig(os.path.join(output_dir, 'traffic_sample_dotplot.png'), dpi=300)
plt.close(fig)

# ---------------------------------------------------------
# Figure 3: Sampling Distribution & p-Value
# ---------------------------------------------------------
fig, ax = plt.subplots(figsize=(9, 5))

df = 4
x = np.linspace(-4.5, 4.5, 1000)
y = stats.t.pdf(x, df)

ax.plot(x, y, color='#2b5c8f', lw=2.5, label=r'Student\'s $t$-distribution ($\text{df}=4$)')

# Rejection region (alpha=0.05 two-tailed -> t_crit = +-2.776)
tcrit = 2.776
x_rej_low = x[x <= -tcrit]
x_rej_high = x[x >= tcrit]
ax.fill_between(x_rej_low, stats.t.pdf(x_rej_low, df), color='#b2182b', alpha=0.6, label=r'Rejection Region ($\alpha = 0.05$, $t_{crit} = \pm 2.776$)')
ax.fill_between(x_rej_high, stats.t.pdf(x_rej_high, df), color='#b2182b', alpha=0.6)

# Observed t = -0.0771
t_obs = -0.0771
ax.axvline(t_obs, color='#e66101', linestyle='-', lw=2.5, label=f'Observed $t = {t_obs:.4f}$')
ax.axvline(-t_obs, color='#e66101', linestyle=':', lw=1.5)

# Highlight p-value area
x_p = x[(x <= -abs(t_obs)) | (x >= abs(t_obs))]
ax.fill_between(x_p, stats.t.pdf(x_p, df), color='#e66101', alpha=0.15, label=f'$p$-value area = 0.942')

ax.set_ylabel('Probability Density', fontweight='bold', fontsize=11)
ax.set_xlabel('$t$-Statistic', fontweight='bold', fontsize=11)
ax.set_title(r'Sampling Distribution & Decision Rule ($t$-test, $\text{df}=4$)', fontweight='bold', fontsize=13, pad=12)
ax.annotate('Observed $t=-0.0771$\n(Well inside non-rejection zone)\n$p$-value = 0.942 > 0.05\nFail to Reject $H_0$',
            xy=(t_obs, 0.25), xytext=(-3.8, 0.28),
            arrowprops=dict(facecolor='#e66101', shrink=0.05, width=1.5, headwidth=8),
            fontsize=9.5, fontweight='bold', bbox=dict(facecolor='white', alpha=0.9, edgecolor='gray'))

ax.legend(loc='upper right', frameon=True)

plt.tight_layout()
fig.savefig(os.path.join(output_dir, 't_distribution_pvalue.png'), dpi=300)
plt.close(fig)

# ---------------------------------------------------------
# Figure 4: Duality of CI and Hypothesis Test
# ---------------------------------------------------------
fig, ax = plt.subplots(figsize=(9, 3.5))

ci_low, ci_high = 4200.57, 5756.23
xbar = 4978.4
mu0 = 5000

ax.plot([ci_low, ci_high], [1, 1], color='#2b5c8f', lw=6, label='95% Confidence Interval [4200.6, 5756.2]')
ax.scatter([xbar], [1], color='#1f78b4', s=140, zorder=5, label=f'Sample Mean (\\bar{{x}} = {xbar:.1f})')
ax.axvline(mu0, color='#b2182b', linestyle='--', lw=2.5, label=r'Hypothesised Value ($H_0: \mu_0 = 5000$)')

ax.annotate(r'$L = 4200.6$', xy=(ci_low, 1), xytext=(ci_low-100, 0.75), fontweight='bold', fontsize=10, color='#2b5c8f')
ax.annotate(r'$U = 5756.2$', xy=(ci_high, 1), xytext=(ci_high-100, 0.75), fontweight='bold', fontsize=10, color='#2b5c8f')
ax.annotate(r'$\mu_0 = 5000$ lies INSIDE the 95% CI' + '\n' + r'$\rightarrow$ Fail to Reject $H_0$ at $\alpha = 0.05$',
            xy=(mu0, 1), xytext=(mu0+150, 1.3),
            arrowprops=dict(facecolor='#b2182b', shrink=0.05, width=1.5, headwidth=8),
            fontweight='bold', fontsize=10, bbox=dict(facecolor='white', alpha=0.9, edgecolor='gray'))

ax.set_ylim(0.5, 1.6)
ax.set_yticks([])
ax.set_xlabel('Mean Daily Traffic Volume (vehicles/day)', fontweight='bold', fontsize=11)
ax.set_title('Duality Between 95% Confidence Interval and Hypothesis Test Decision', fontweight='bold', fontsize=13, pad=12)
ax.legend(loc='lower right', frameon=True)

plt.tight_layout()
fig.savefig(os.path.join(output_dir, 'ci_hypothesis_duality.png'), dpi=300)
plt.close(fig)

# ---------------------------------------------------------
# Figure 5: Before-After Visual for Paired t-Test
# ---------------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 5))

routes = np.arange(1, 9)
before = np.array([14.2, 16.5, 12.8, 18.1, 15.0, 17.4, 13.9, 19.0])
after  = np.array([12.5, 15.0, 13.1, 15.4, 13.8, 15.2, 13.5, 16.1])

for i in range(len(routes)):
    diff = after[i] - before[i]
    color = '#e66101' if diff < 0 else '#2b5c8f'
    ax.plot([1, 2], [before[i], after[i]], color=color, marker='o', lw=2, alpha=0.8)
    ax.text(0.95, before[i], f'R{routes[i]}: {before[i]}', ha='right', va='center', fontsize=9)
    ax.text(2.05, after[i], f'{after[i]} ({diff:+.1f})', ha='left', va='center', fontsize=9, fontweight='bold' if diff < 0 else 'normal')

ax.set_xticks([1, 2])
ax.set_xticklabels(['Before Intervention', 'After Intervention'], fontweight='bold', fontsize=11)
ax.set_ylabel('Travel Time (minutes)', fontweight='bold', fontsize=11)
ax.set_title('Paired Travel Time Differences ($d_i = \\text{After}_i - \\text{Before}_i$)', fontweight='bold', fontsize=13, pad=12)
ax.set_xlim(0.7, 2.3)
ax.grid(axis='x')

ax.plot([], [], color='#e66101', marker='o', lw=2, label='Decreased Travel Time (7/8 routes)')
ax.plot([], [], color='#2b5c8f', marker='o', lw=2, label='Increased Travel Time (1/8 routes)')
ax.legend(loc='upper right', frameon=True)

plt.tight_layout()
fig.savefig(os.path.join(output_dir, 'paired_travel_times.png'), dpi=300)
plt.close(fig)

# ---------------------------------------------------------
# Figure 6: Normality Diagnostic Q-Q Plot
# ---------------------------------------------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 5))

np.random.seed(20)
norm_data = np.random.normal(0, 1, 40)
skew_data = np.random.exponential(1.5, 40)

(osm1, osr1), (slope1, intercept1, r1) = stats.probplot(norm_data, dist="norm")
ax1.plot(osm1, osr1, 'o', color='#2b5c8f', alpha=0.8)
ax1.plot(osm1, slope1 * np.array(osm1) + intercept1, color='#b2182b', lw=2, linestyle='--')
ax1.set_title('A. Normally Distributed Sample\n(Points align closely along 45° line)', fontweight='bold', fontsize=11)
ax1.set_xlabel('Theoretical Quantiles', fontweight='bold', fontsize=10)
ax1.set_ylabel('Sample Quantiles', fontweight='bold', fontsize=10)

(osm2, osr2), (slope2, intercept2, r2) = stats.probplot(skew_data, dist="norm")
ax2.plot(osm2, osr2, 'o', color='#e66101', alpha=0.8)
ax2.plot(osm2, slope2 * np.array(osm2) + intercept2, color='#b2182b', lw=2, linestyle='--')
ax2.set_title('B. Heavily Skewed Sample\n(Points curve systematically away from line)', fontweight='bold', fontsize=11)
ax2.set_xlabel('Theoretical Quantiles', fontweight='bold', fontsize=10)

plt.suptitle('Normal Q-Q Plot Diagnostics for Assessing Normality Assumption', fontweight='bold', fontsize=13, y=1.02)
plt.tight_layout()
fig.savefig(os.path.join(output_dir, 'qq_plot_diagnostics.png'), dpi=300)
plt.close(fig)

print("All 6 figures generated successfully in:", output_dir)
