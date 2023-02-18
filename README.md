# Report for assignment 3

This is the report repository for Assignment 3.
For the forked repository of the project, see [zsabbagh/algorithms](https://github.com/zsabbagh/algorithms).

## Contributions and Goals

- Zakaria: **Goal is to achieve P+**.
- Glacier: **Goal is to achieve atleast a P**
- Einar: **Goal is to achieve P or P+**.

## Project

Name: Algorithms

URL: [keon/algorithms](https://github.com/keon/algorithms)

It is a collection of algorithms and data structure for Python3.

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

There are however several functions and files which are not tested at all. This was discovered when checking the branch coverage by using our own branch coverage tool.
For example, `red_black_tree.py` which we chose two functions from ( `delete_fixup` and `fix_insert`) with relativly high cyclomatic complexity, had no unittests.

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

We interpreted second P requirement
"You also manually count the complexity of five functions (on paper or as comments)"
as being scalable to the group count.
Currently, the three (currently) active members then propose that
we would need to count three functions, with six presented.
The chosen functions (so far) is, with results:

```
maximum_flow_bfs @ 28-87 @ ../algorithms/algorithms/graph/maximum_flow_bfs.py
   NLOC     30
   CCN      10
   Einar    7
   Glacier  7

delete_fixup@209-267@../algorithms/algorithms/tree/red_black_tree/red_black_tree.py
	NLOC     47.0
	CCN      18.0

edmonds_karp @ algorithms/graph/maximum_flow.py
   NLOC     33
   CCN      12

fix_insert @ algorithms/tree/red_black_tree/red_black_tree.py
   NLOC     35
   CCN      11

sort_diagonally @ algorithms/matrix/sort_matrix_diagonally.py
   NLOC     35
   CCN      10
   Zakaria  8
   Glacier  8

knuth_morris_pratt @ algorithms/strings/knuth_morris_pratt.py
   NLOC     40
   CCN      11
   Zakaria  9
   Einar    11
```

### What are your results for ten complex functions?
ALl methods did not get the same result.
Lizard got +2 extra on `sort_diagonally`, which we did not realise why.
Furthermore, `knuth_morris_pratt` differed with +2 as well.
After testing, it was clear that Lizard counts `[ 0 for _ in range(m) ]` as
a CCN increment.
However, it could be argued that this is incorrect, since the statement
is equivelant to `[0] * m`.
Moreover the results are clear.

### Are the functions just complex, or also long?

They are relatively long.
However, lizard includes comments, which
means that the effective NLOC would be significantly
lower considering the amount of function documentation
this project has.

### What is the purpose of the functions?

- `knuth_morris_pratt` is a string-searching function for counting
word occurrences.
- `sort_matrix_diagonally` sorts a matrix with regards to a diagonal
position, i.e. with regards to the lowest value of either column
or row position.
- `fix_insert` is an insertion algorithm for the red-black tree
data structure.
- `edmond_karp` is a function to find the maximal flow throw a directed
graph.
- `delete_fixup` deletes a node in the red-black tree data structure.
- `maximum_flow_bfs` is an algorithm for calculating maximum flow
of a graph using breadth-first search.


### Are exceptions taken into account in the given measurements?
There are no `raise Error` in the code measured.
However, by the tool used, lizard, it does not seem to measure
raising errors as an increase of CCN.
Practically, it seems logical to exclude exceptions from
the CCN calculations, as it is only a new direct exit-point.

### Is the documentation clear w.r.t. all the possible outcomes?
Generally, no. Sort-diagonally is not very clearly described,
neither does it include a function comment.
But this seems like a common practice.
At least, it is not particularly clear of the branching in
each function.
However, the algorithms are widely known, meaning
that they might not need descriptions to that extent.
Further researching of algorithms could be done online.

## Refactoring

Below are several areas of improvement and refactoring
discussed.

### Refactoring of code

There are indeed several repetitions of rudimentary algorithms,
for example BFS is one that occurs multiple times in several
different modules / paths.
However, there are distinct purposes and minor modifications in the algorithm,
and refactoring each and re-using such code would make each
algorithm collection which re-uses such functions be co-dependent
on the functionality of one-single function.
Modification of the function and correctness would then
depend on it, as a result, which in turn would make the project
less easy to add upon.
The beauty of the current structure, although repetition occurs,
is that each collection functions similarly to an own library
or "sub-library", making it easier to contribute to and build
on the collection.

### Optimisation of list-creation

`knuth_morris_pratt` optimisation
There is a simple line that could lower the complexity.
Changing `[0 for i in range(m)]` to `[0] * m` would lower the
complexity according to `lizard` by 1.
According to [GeeksForGeeks](https://www.geeksforgeeks.org/python-which-is-faster-to-initialize-lists/),
their measure states that using the list comprehension technique
would be roughly 17.7 times slower than using
the star operator.
Our own benchmarks (script file is `./scripts/bench.py`) propose similar results.
With a list-size of 1 million, comprehension is roughly
20-24 times slower.
For this reason, it does not only give a lower cyclomatic complexity
(which really might not make any difference) by altering the code
as such, but more importantly it optimises the algorithm.

It is important to note that this is not a one-time occurrence
in the project.
There are 46 *potential* candidate lines to alter
(detected with `grep -r -E "\[.*for.*range.*\]" | grep -v "\*"` command).
Alas, the star-operator does however create copies of references
when used nested.
For this reason, it is only possible to use it on the inner most
array, or else the arrays would be copies of each other.

## Coverage

### Tools

Document your experience in using a "new"/different coverage tool.

How well was the tool documented? Was it possible/easy/difficult to
integrate it with your build environment?

### Your own coverage tool

TODO

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

We actually worked with all 6 functions when checking the coverage, as several of these already had 100% branch coverage.
This, inorder for us to screen for appropriate functions to implement unittests for. 
What we ultimately found was the functions in the RBT class, together with 
`def sort_matrix_diagonally` did not have 100% coverage.
In the case of RBT, the coverage was trivially improved by adding unittests, since these did not exist.


Report of old coverage: [link]

Report of new coverage: [link]

Test cases added:

git diff ...

Number of test cases added: two per team member (P) or at least four (P+).


**Glacier:**
- `sort_matrix_diagonally.py: test_sort_diagonally_with_vector`, a trivial test which checks the first identified branch. Specifically, if a matrix with 1 row or 1 column (vector) is provided as input, the entire vector should be returned.
- TODO

## Self-assessment: Way of working

TODO

Current state according to the Essence standard: ...

Was the self-assessment unanimous? Any doubts about certain items?

How have you improved so far?

Where is potential for improvement?

## Overall experience

The key take-aways from this project is the idea of branch and code coverage.
It is immensely clever to be able to measure how *efficiently* the
crafted unit-tests actually covers and tests the written code.
It also provides certainty that the crafted tests are thought out
and has a purpose.
Quality is to be preferred when considering tests, not necessarily
quantity, since tests which monitors the same code and are
algorithmically identical does not ensure code quality.

## P+ Contribution

TODO
