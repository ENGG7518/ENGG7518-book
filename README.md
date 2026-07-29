# ENGG7518: Research Methods for Engineers

📖 **Read the online book:** [https://engg7518.github.io/ENGG7518-book/](https://engg7518.github.io/ENGG7518-book/)  
🎓 **Official UQ Course Profile:** [ENGG7518 Course Profile](https://course-profiles.uq.edu.au/course-profiles/ENGG7518-62269-7660)

Welcome to the source repository for the **ENGG7518: Research Methods for Engineers** course book at The University of Queensland.

> [!IMPORTANT]
> **Work in Progress Notice**: This course book is currently a draft and work in progress. If you spot any problems or inconsistencies, please [report an issue on GitHub](https://github.com/ENGG7518/ENGG7518-book/issues), email Dr. Weiming Zhao ([weiming.zhao@uq.edu.au](mailto:weiming.zhao@uq.edu.au)), or refer to the official [UQ Course Profile](https://course-profiles.uq.edu.au/course-profiles/ENGG7518-62269-7660) and primary course materials on Blackboard.

This repository contains the source code for the open course book, built using [Quarto](https://quarto.org/). It provides lecture notes, reading materials, and practical R tutorials covering research methodology, applied statistics, and numerical optimisation.

## Course Structure

The course materials are divided into four main modules:

1. **Course Administration**: Overview, assessments, communication guidelines, and software setup.
2. **Research Fundamentals**: The nature of scientific enquiry, Mertonian norms, logic & reasoning, research design, and literature reviews.
3. **Statistics & Reproducibility**: Descriptive and inferential statistics, reproducible analysis with R and Quarto, and regression modelling.
4. **Data & Optimisation**: Data processing, quality control, classical optimisation methods, and numerical methods (e.g., Newton's method).

## Teaching Team

- **Course Coordinator & Lecturer**: Prof. Zuduo Zheng ([zuduo.zheng@uq.edu.au](mailto:zuduo.zheng@uq.edu.au))
- **Lecturer**: Dr Weiming Zhao ([weiming.zhao@uq.edu.au](mailto:weiming.zhao@uq.edu.au))
- **Tutor**: Dr Saeed Mohammadian ([s.mohammadian@uq.edu.au](mailto:s.mohammadian@uq.edu.au))

## Repository Structure

- `admin/`: Course administration and overview materials.
- `fundamentals/`: Modules on research fundamentals and methodology.
- `stats/`: Statistics, reproducibility, and regression modelling modules.
- `optimisation/`: Engineering optimisation and numerical methods.
- `tutorials/`: Hands-on tutorial labs (e.g., Introduction to R).
- `images/`: Images and static assets used throughout the book.
- `index.qmd` & `_quarto.yml`: The main entry point and Quarto project configuration.
- `references.bib`: The bibliography for the course book.

## Building the Book Locally

To build and preview the book on your local machine, you will need to have [Quarto](https://quarto.org/docs/get-started/) installed, as well as [R](https://www.r-project.org/) if you intend to execute the R code chunks.

1. Clone this repository:
   ```bash
   git clone https://github.com/ENGG7518/ENGG7518-book.git
   ```
2. Navigate to the project directory:
   ```bash
   cd ENGG7518-book
   ```
3. Preview the book (this will open a live preview in your web browser):
   ```bash
   quarto preview
   ```
4. Render the book (outputs to the `_book/` directory by default):
   - **Render all formats** (both HTML and Typst PDF):
     ```bash
     quarto render
     ```
   - **Render HTML format only**:
     ```bash
     quarto render --to html
     ```
   - **Render Typst PDF format only**:
     ```bash
     quarto render --to typst
     ```

## License and Copyright

© 2026 The University of Queensland | School of Civil Engineering
