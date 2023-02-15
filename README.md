# Report for assignment 3

This is a template for your report. You are free to modify it as needed.
It is not required to use markdown for your report either, but the report
has to be delivered in a standard, cross-platform format.

## Project

Name: Algorithms

URL: https://github.com/keon/algorithms

It is a algorithms and data structure library for Python3.

## Onboarding experience

The project does fulfill the requirements,
and although there are duplicate entries in the 
Google Sheets, an email confirmation by Cyrille
verified that we could continue with this 
project although other groups might start working on it.

### Dependencies

The first thing that was noticed was that cloning
`keon/algorithms` did not directly state what dependencies
was required to run the tests. 
Although minor, `pytest` was required to be installed before 
the tests could be run properly.
Thus, the command `pip3 install pytest` is required for 
running the unit-tests described in the documentation.

### Building

It was very easy to build the library, considering
it was basically installed with `pip3 install` and
then possible to be included in the code.
It was easy to import a certain algorithm, as it was
simply just to do `from algorithms import ...`.

### Documentation

The documentation was not magnificent.
It was in the form of function comments and not available
through a more sophisticated website, pdf or markdown document.

### Errors

There has been no error recorded yet, except the 
one referred to under `Dependencies`.

### Tests

The library's tests runs well on the 
current system (macOS Monterey 12.2.1).

### Continuation

As this project seems feasible to grasp,
and is reasonably well-documented, we will most
likely continue with it.


#### Questions

Did it build and run as documented?

See the assignment for details; if everything works out of the box,
there is no need to write much here. If the first project(s) you picked
ended up being unsuitable, you can describe the "onboarding experience"
for each project, along with reason(s) why you changed to a different one.


## Complexity

The chosen functions (so far) is:

```
ladder_length @ 24-64 @ ../algorithms/algorithms/bfs/word_ladder.py
valid_solution_hashtable @ 17-44 @ ../algorithms/algorithms/matrix/sudoku_validator.py
invert_matrix @ 26-63 @ ../algorithms/algorithms/matrix/matrix_inversion.py
maximum_flow_dfs @ 27-87 @ ../algorithms/algorithms/graph/maximum_flow_dfs.py
maximum_flow_bfs @ 28-87 @ ../algorithms/algorithms/graph/maximum_flow_bfs.py
find_k_factor @ 33-85 @ ../algorithms/algorithms/dp/k_factor.py
edmonds_karp @ 51-90 @ ../algorithms/algorithms/graph/maximum_flow.py
fix_insert @ 88-141 @ ../algorithms/algorithms/tree/red_black_tree/red_black_tree.py
sort_diagonally @ 25-77 @ ../algorithms/algorithms/matrix/sort_matrix_diagonally.py
knuth_morris_pratt @ 3-44 @ ../algorithms/algorithms/strings/knuth_morris_pratt.py
```

1. What are your results for ten complex functions?
   * Did all methods (tools vs. manual count) get the same result?
   * Are the results clear?
2. Are the functions just complex, or also long?
3. What is the purpose of the functions?
4. Are exceptions taken into account in the given measurements?
5. Is the documentation clear w.r.t. all the possible outcomes?

## Refactoring

Plan for refactoring complex code:

Estimated impact of refactoring (lower CC, but other drawbacks?).

Carried out refactoring (optional, P+):

git diff ...

## Coverage

### Tools

Document your experience in using a "new"/different coverage tool.

How well was the tool documented? Was it possible/easy/difficult to
integrate it with your build environment?

### Your own coverage tool

Show a patch (or link to a branch) that shows the instrumented code to
gather coverage measurements.

The patch is probably too long to be copied here, so please add
the git command that is used to obtain the patch instead:

git diff ...

What kinds of constructs does your tool support, and how accurate is
its output?

### Evaluation

1. How detailed is your coverage measurement?

2. What are the limitations of your own tool?

3. Are the results of your tool consistent with existing coverage tools?

## Coverage improvement

Show the comments that describe the requirements for the coverage.

Report of old coverage: [link]

Report of new coverage: [link]

Test cases added:

git diff ...

Number of test cases added: two per team member (P) or at least four (P+).

## Self-assessment: Way of working

Current state according to the Essence standard: ...

Was the self-assessment unanimous? Any doubts about certain items?

How have you improved so far?

Where is potential for improvement?

## Overall experience

What are your main take-aways from this project? What did you learn?

Is there something special you want to mention here?

