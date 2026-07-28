# Figure Management & Generation Guide

This directory (`quarto_files/images/`) contains static visual assets and standalone generation scripts for the online textbook.

## Figure Management Workflows

Figures in this course book are managed through two distinct approaches depending on complexity, build performance, and source readability:

---

### Approach 1: External Script-Generated Figures (Static Assets)
* **Image Output:** `quarto_files/images/*.png`
* **Source Scripts:** `quarto_files/images/scripts/`
* **Best Used For:** Complex, highly-styled, multi-panel diagrams or heavily annotated statistical illustrations that require extensive plotting code.
* **Advantages:** 
  - Keeps `.qmd` chapter source files clean, narrative-focused, and concise.
  - Ensures fast `quarto render` build times (does not re-execute heavy plotting code during every build).
  - Environment-independent rendering for reviewers who may lack specific Python packages.

#### Registered External Scripts:
| Script Path | Chapter / Module | Generated PNG Assets |
| :--- | :--- | :--- |
| `images/scripts/generate_week5_basic_stats_figures.py` | **Statistics Basics & Hypothesis Testing** (`stats/week5_basic-statistics.qmd`) | `ci_repeated_sampling.png`<br>`traffic_sample_dotplot.png`<br>`t_distribution_pvalue.png`<br>`ci_hypothesis_duality.png`<br>`paired_travel_times.png`<br>`qq_plot_diagnostics.png` |
| `images/scripts/generate_week8_data_cleaning_figures.py` | **Data Quality & Cleansing** (`stats/week8_data-cleaning-and-quality.qmd`) | `boxplot_fences.png`<br>`masking_swamping.png`<br>`missing_data_mechanisms.png`<br>`moving_average_smoothing.png` |
| `images/` (Static Assets) | **Research Fundamentals & Reproducibility** (`fundamentals/`, `stats/`) | `research-process.png`<br>`reproducibility_spectrum.png` |

#### How to Re-generate External Figures:
Execute the script from the project root or script directory:
```bash
python3 quarto_files/images/scripts/generate_week5_basic_stats_figures.py
python3 quarto_files/images/scripts/generate_week8_data_cleaning_figures.py
```

#### Markdown Reference Syntax in `.qmd`:
```markdown
![Caption Text](../images/ci_repeated_sampling.png){#fig-ci-sampling}
```

---

### Approach 2: Embedded Code Chunks (Dynamic Figures)
* **Location:** Directly inside `.qmd` files (`stats/`, `optimisation/`, etc.).
* **Best Used For:** Simple exploratory data plots, code demonstrations shown to students, and flowcharts.
* **Advantages:** Automatically updates upon rendering if underlying datasets or code change.

#### A. R / Python Code Blocks
Used for interactive examples and direct statistical code output.
```markdown
```{r}
#| label: fig-scatter-example
#| fig-cap: "Scatterplot of variables"
#| echo: false
plot(x, y)
```
```

#### B. Mermaid Diagram Blocks
Used for process flows, decision trees, and methodology flowcharts.
```markdown
```{mermaid}
%%| label: fig-research-flow
%%| fig-cap: "The Research Process Flowchart"
graph TD
    A[Formulate Hypothesis] --> B[Data Collection]
    B --> C[Data Quality & Cleansing]
    C --> D[Statistical Modelling]
```
```
