# Report for assignment 3

This is the report repository for Assignment 3.
For the forked repository of the project, see [zsabbagh/algorithms](https://github.com/zsabbagh/algorithms).

## Contributions and Goals

- Zakaria: **Goal is to achieve P+**.
    - Added 6+ tests to `red_black_tree` to improve coverage from 0 to 60+ %.
    - Refactor and redesign `red_black_tree` class to abstract away the structure.
    - Write parser under `scripts/` for sorting `lizard` output.
    - Write scripts to visualise untested data, seen under the forked project `zsabbagh/algorithms/scripts/untested.py` under branch `1-coverage`.
- Glacier: **Goal is to achieve a P**
   -  Performed manual calculation of cyclomatic complexity on `maximum_flow_bfs` and `sort_diagonally`.
   - Implemented our own coverage tool on `sort_diagonally` and `fix_insert`.
   - Refactoring plan for `sort_diagonally`.
   - Added 2 unittests in total to `sort_diagonally` and `bellman_ford`.
   - General contribution to report/README
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

The calculations could be seen below:
- `knuth_morris_pratt`, [Zakaria's calculation](https://lucid.app/lucidchart/d0f90c25-8db7-45a8-bd66-623e3d775f7a/edit?invitationId=inv_9628e855-787b-463b-851b-ddb0e51a94a0&page=0_0#)
- `knuth_morris_pratt`, [Einar's calculation](https://lucid.app/lucidchart/14755430-cef5-4828-a84e-c21b87b93109/edit?viewport_loc=167%2C213%2C1675%2C969%2C0_0&invitationId=inv_2bb531b9-3be1-4811-a8e3-afd93101dcf3)
  - NOTE: These two differs, and the reason for this is the `end_while` and `end_for` statements. This has been discussed with TA's, hence a third calculation is left out.
- `sort_diagonally`, [Zakaria's calculation](https://lucid.app/lucidchart/d0f90c25-8db7-45a8-bd66-623e3d775f7a/edit?invitationId=inv_9628e855-787b-463b-851b-ddb0e51a94a0&page=0_0#)
- `sort_diagonally`, [Glacier's calculation](https://docs.google.com/drawings/d/1en_R6TV2XD9jaH4AVHL-HzCMciKB8RFHzMa2YeVrVvM/edit?usp=sharing)
- `maximum_flow_bfs`, [Einar's calculation](https://lucid.app/lucidchart/b9a655e3-3892-4ab9-a88b-6881475cb1da/edit?viewport_loc=64%2C-45%2C1675%2C969%2C0_0&invitationId=inv_384df42b-2a9a-48f8-be8e-171e4a5f38b3)
- `maximum_flow_bfs`, [Glacier's calculation](https://lucid.app/lucidchart/d289c24f-e856-43bc-9626-f3a07b6edee1/edit?viewport_loc=-387%2C-1142%2C2313%2C1032%2C0_0&invitationId=inv_369dfd6a-a90d-40a1-a6d5-2cc7775bdc5b)

### What are your results for ten complex functions?
All methods did not get the same result.
Lizard got +2 extra on `sort_diagonally`, which we did not understand why.
Furthermore, `knuth_morris_pratt` differed with +2 as well.
After testing, it was clear that Lizard counts `[ 0 for _ in range(m) ]` as
a CCN increment.
However, it could be argued that this is incorrect, since the statement
is equivelant to `[0] * m`.

It could also be argued that Lizard sees this as a basic for loop: 
```
for i in range m:
   a[i] = 0
```
Thus, this would be a predicate/branching, since we either enter the loop, or exit to next section of the code, adding cyclomatic complexity.

The mainly chosen method to calculate the complexity by hand, was to plot a flow graph of the funciton, and count the number of closed regions.
We also had some differing results amongst ourselves and our own calculations.
This was partly due to how the flow graphs were plotted. For example some differing intepertations where wheter an `end-while` or `end-for` statement should have been included in the graph as a node. While others chose to plot the flow graphs as condensations graphs. There where also other methods other than that we used, which would give slightly different results. In general though, the complxity did not vary greatly in our calculations and Lizards.

[Source for our used methods.](https://www.bbau.ac.in/dept/CS/TM/Cyclomatic.pdf])

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
- `fix_insert` is a helper function for the insertion algorithm of the red-black tree
data structure.
- `edmonds_karp` is a function to find the maximal flow throw a directed
graph.
- `delete_fixup` is a helper function for the deletion algorithm
in the red-black tree data structure.
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


**sort_matrix_diagonally.py**: One example to simplify it's complexity, is to extract the this part:
```
while h:
   ele = heappop(h)
   mat[row][col] = ele
   row += 1
   col += 1
```
This snippet of code sorts the diagonal, and is executed in two seperate conditions. Either when the algorithm is processing the rows, or when it is processing the columns.
A concrete improvement could be to extract the logic to a function which is called, and which takes the necessary information like the row, column, heap and matrix as arguments.

**red_black_tree.py**: There is an issue concerning this data structure. The data structure does not currently
"wrap" values, but rather needs an `RBNode` to insert.
This is problematic and should really be resolved, as the functionality of the data structure now relies
on intricacies which the class should abstract. For example:
```
def insert(self, node):
```
Clearly takes in a node. This should really take in a `value` of which one wants to store.
Further, there are already refactoring taking place, where `delete_fixup` is such a
refactoring of the `delete` algorithm and `fix_insert` fixes the `insert`.
This is to preserve colouring and the structure of the tree.
However, as they are meant to be *private* functions, they should really be named
`_delete_fixup`, i.e. the convention of naming for supposed-to-be private functions.
This would clarify the purpose of them refactoring the code for each of the functions.
Similarly, `left_rotate` and `right_rotate` does refactor the fixing functions,
which proposes that they also should be private.
`RBTree` did not automatically wrap values, but rather took in nodes.
This does not abstract away nodes as data structures.
A plan is to refactor/redesign `red_black_tree` to function as such.


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

- One limitation of the tool is simple if statements in the code with no explicit else statements. Our tool would not recognize the alternative branch (corresponding to an else) if it does not explicitly say so.

- Another limitation is that the tool wont work on ternary operators.

- A third limitation which was discovered during the improvement of coverage, is early return statements. The tool writes and compiles the final report of covered branches in the end of the function right before a return. In `sort_matrix_diagonally.py` one branch (an if-statement) was included in the coverage report as missing. After adding a unittest, this was still the case (using our own tool). This was due to the fact that the function returned immidiately if it stepped into the statement, thus never reporting/writing the coverage. To solve this we'd have to add the reporting before each return statement, or we would have to have to rewrite the function making sure that all returns are made after the coverage reporting.

3. Are the results of your tool consistent with existing coverage tools?

## Coverage improvement

Show the comments that describe the requirements for the coverage.

We actually worked with all 6 functions when checking the coverage, as several of these already had 100% branch coverage.
This, inorder for us to screen for appropriate functions to implement unittests for.
What we ultimately found was the functions in the RBT class, together with
`def sort_diagonally` did not have 100% coverage.
In the case of RBT, the coverage was trivially improved by adding unittests, since these did not exist.


Report of old coverage: [link]

Report of new coverage: [link]

Test cases added:

git diff ...

Number of test cases added: two per team member (P) or at least four (P+).


**Glacier:**
- `sort_matrix_diagonally.py: test_sort_diagonally_with_vector`, a trivial test which checks the first identified branch. Specifically, if a matrix with 1 row or 1 column (vector) is provided as input, the entire vector should be returned as it is. The old branch coverage using coverage.py, was reported fass 94%. The new coverage was reported as 100%.

- `bellman_ford.py: test_bellman_ford_no_shortest_path` The `bellman_ford` function was not originally one of our chosen functions. However, due to many of them already having 100% branch coverage, this function was later retrieved with the sole purpose of improving branch coverage. The previous branch coverage was according to the general tool coverage.py report: 94%. There were no tests checking if there was no valid solution. The added test is therefore a graph with a negative cycle and should result in `false`. The function now has 100% branch coverage.
**Note: the function also has a high cyclomatic complexity of 8**

**Zakaria**
- `red_black_tree`, including `fix_insert` and `delete_fixup`, was previously 0% tested, with other words it did not even show up when the tests were run. Now the tests cover more than 70% of the entire code, i.e. all of the class methods.

**Einar**
- `knuth_morris_pratt` had 90% branch coverage, with one branch missing being tested. That branch was a while-loop within the making of the pi table. To enter the while-loop a specific condition must be met for the input pattern, there have to appear two identical letters in a row, followed by a letter that does not match. After creating the test case with the input parameter text being `aaaaaaa` and the pattern being `aabb` the test coverage increased to 100%.

- Since adding only one test meant it had full branch coverage, I began thinking about the path coverage.

  - I noticed there was not a single test where no letter from the pattern matched the text, so a test case for that was added. I also noticed there was not a test case where the text and pattern differ in data types. So I added a test case where the text is a list of integers and the pattern is a string. Those two are the first test cases where the first if-statement within the finding a pattern section is not entered.

  - I also noticed that there were no test cases where either the text or pattern (or both) were an empty string. This greatly alters the path taken since it affects if the for-loops are entered when making the pi table and finding a pattern.
    - Adding a test case where both are empty strings skips both loops.
    - If the text is an empty string but not the pattern, we only make the pi table but skip finding a pattern.
    - After adding a test case where the pattern is an empty string but not the text something interesting happened. The making of the pi table is skipped but within the for-loop for finding a pattern, an exception gets raised. That is because a letter from the text is compared to an indexed empty string.


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
