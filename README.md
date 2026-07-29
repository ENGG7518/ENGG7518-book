# ENGG7518: Research Methods for Engineers

Welcome to the source repository for the **ENGG7518: Research Methods for Engineers** course book at The University of Queensland.

This repository contains the source code for the online course book, which is built using [Quarto](https://quarto.org/). It serves as the central hub for course notes, lecture materials, research principles, statistical foundations, data processing methods, and numerical optimisation techniques.

## Course Structure

The course materials are divided into four main modules:

1. **Course Administration**: Overview, assessments, communication guidelines, and software setup.
2. **Research Fundamentals**: The nature of scientific enquiry, Mertonian norms, logic & reasoning, research design, and literature reviews.
3. **Statistics & Reproducibility**: Descriptive and inferential statistics, reproducible analysis with R and Quarto, and regression modelling.
4. **Data & Optimisation**: Data processing, quality control, classical optimisation methods, and numerical methods (e.g., Newton's method).

## Teaching Team

- **Course Coordinator & Lecturer**: Prof. Zuduo Zheng
- **Lecturer**: Dr Weiming Zhao
- **Tutor**: Dr Saeed Mohammadian

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
4. Render the book completely (outputs to the `_book/` directory by default):
   ```bash
   quarto render
   ```

## License and Copyright

© 2026 The University of Queensland | School of Civil Engineering
