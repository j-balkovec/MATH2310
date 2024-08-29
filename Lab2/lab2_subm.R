"_brief_

_course_: MATH 2310
_author_: Jakob Balkovec
_instructor_: G. Egan

_file_: lab2_subm.R (R_scipt, not Rmd Notebook)

_brief_: Discrete Distributions in R

_notes_:
  - Probabiity Density func       [dbinom()]
  - Cummulative distribution func [pbinom()]
  - Quantile func                 [qbinom()]
  - Random sampling func          [rbinom()]
"

install.packages("pracma")
library(pracma)

# Define the function symbolically
f <- expression(x^2)

# Integrate symbolically
result <- integrate(f, "x")

# Print the result
print(result)