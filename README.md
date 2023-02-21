# Report for assignment 3

This is the report repository for Assignment 3.
For the forked repository of the project, see [zsabbagh/algorithms](https://github.com/zsabbagh/algorithms).

## Contributions and Goals

- Zakaria: **Goal is to achieve P+**.
    - Calculated cyclomatic complexity manually of functions.
    - P+: Added 7+ tests to `red_black_tree` to improve coverage from 0 to 79 %.
    This includes `delete_fixup` and `fix_insert`, which had 0% coverage previously.
    - P+: Refactor `strip_url_params1` from a complexity of 20 to a complexity of 6. See [new file](https://github.com/zsabbagh/algorithms/blob/refactoring/algorithms/strings/strip_url_params.py) compared to [old file](https://github.com/zsabbagh/algorithms/blob/master/algorithms/strings/strip_url_params.py).
    This refactoring is not necessary, but does decrease complexity without changing functionality.
    - P+ (extraordinary): Refactor and redesign [`red_black_tree`](https://github.com/zsabbagh/algorithms/blob/3-new-tests/algorithms/tree/red_black_tree/red_black_tree.py) class to abstract away the structure.
        - What this means exactly, is that the class previously took in `RBNode`s as input during insertion
        and deletion, which does *not* abstract away the data structures functionality.
        The change now makes the function actually treat values rather than nodes, and the added
        tests verifies this functionality.
        - This includes refactoring of the `RBNode` class to exist within the `RBTree` class.
        Also, core functionality has been added and correctness has been improved and verified.
        - Fixed implementation bugs such as deleting leaf-nodes raised errors.
        - Added tests that verify new functionality.
    - P+: Been actively contributing to the project since the first day, with
    consistent work using GitHub and issue tracking.
    - Wrote parser under [`scripts/parser.py`](scripts/parser.py) for sorting `lizard` output. This sorts and filters
    CCN and NLOC on spans. Further, one could sort on proportion of CCN/NLOC or NLOC/CCN.
    - Wrote scripts to visualise untested data [`scripts/untested.py`](https://github.com/zsabbagh/algorithms/blob/1-coverage/scripts/untested.py).
        - The file lies in the forked project's branch `1-coverage` under the directoriy `scripts/`.
        This is done by searching through the file system and check visited `.py` files by the `Coverage.py` report.
        - The script is run with `py untested.py <path-to-report-file> -u[|--untested] [-t|--tested]`.
- Glacier: **Goal is to achieve a P**
   -  Performed manual calculation of cyclomatic complexity on `maximum_flow_bfs` and `sort_diagonally`.
   - Implemented our own coverage tool on `sort_diagonally` and `fix_insert`.
   - Refactoring plan for `sort_diagonally`.
   - Added 2 unit tests in total to `sort_diagonally` and `bellman_ford`.
   - General contribution to report/README
- Einar: **Goal is to achieve P**.
   - Calculated cyclomatic complexity on `knuth_morris_pratt` and `maximum_flow_bfs` by creating flow charts.
   - Implemented a branch coverage tool for `knuth_morris_pratt` and `edmonds_karp`.
   - Implemented a script, `scripts/branch_coverage_data_parser.py`, to read from our generated data file.
   - Added 4 unit tests for `knuth_morris_pratt`, 1 to reach 100% branch coverage and 3 for path coverage.
   - Refactoring plan for `maximum_flow_bfs`.
   - General contribution to report/README


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

Einar found an error in one function that is described under the `Coverage improvement` chapter when writing unit tests.
An error was also detected in the red black tree class when a leaf node was deleted.

### Tests

The library's tests runs well on the
current system (macOS Monterey 12.2.1).

There are however several functions and files which are not tested at all. This was discovered when checking the branch coverage by using our own branch coverage tool.
For example, `red_black_tree.py` which we chose two functions from ( `delete_fixup` and `fix_insert`) with relativly high cyclomatic complexity, had no unit tests.

### Continuation

As this project seems feasible to grasp,
and is reasonably well-documented, we will most
likely continue with it.

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
Many of these functions follow an algorithm described by a specification which require multiple branches to fulfill and solve complex problems.
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


**sort_matrix_diagonally.py**: One example to simplify its complexity, is to extract the this part:
```
while h:
   ele = heappop(h)
   mat[row][col] = ele
   row += 1
   col += 1
```
This snippet of code sorts the diagonal, and is executed in two seperate conditions. Either when the algorithm is processing the rows, or when it is processing the columns.
A concrete improvement could be to extract the logic to a function which is called, and which takes the necessary information like the row, column, heap and matrix as arguments. The matrix could be returned, or sorted in place.

**red_black_tree.py**: A lot of refactoring is already done in this class.
`fix_insert` and `delete_fixup` refactors the
insert and deletion methods. Furthermore,
`left_rotate` and `right_rotate` refactors
both `fix_insert` and `delete_fixup`.
`transplant` is also a refactorisation of `delete`.
For this reason, refactoring has already been heavily
applied in the class, to the extent which is reasonable,
and further refactoring might not be good practice.

Further refactoring would rather make debugging more difficult, as the refactored code would not have a clear and well-defined purpose.
This is why `left_rotate`, for example, is a reasonable code sequence to refactor - it has a clear purpose and solves something that is repeated multiple times throughout the class' methods.

There is an issue concerning this data structure. The data structure does not currently
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

**maximum_flow_bfs**: This function can be broken down into two seperate functions, one to find a path using BFS and one to use the path outcome to calculate maximum flow. For example:
```
def find_path(new_array):
   #save visited nodes
   visited = [0]*len(new_array)
   #save parent nodes
   path = [0]*len(new_array)

   #initialize queue for BFS
   bfs = queue.Queue()

   #initial setting
   visited[0] = 1
   bfs.put(0)

   #BFS to find path
   while bfs.qsize() > 0:
      #pop from queue
      src = bfs.get()
      for k in range(len(new_array)):
            #checking capacity and visit
            if(new_array[src][k] > 0 and visited[k] == 0 ):
               #if not, put into queue and chage to visit and save path
               visited[k] = 1
               bfs.put(k)
               path[k] = src

   return visited, path
```
The now lighter `maximum_flow_bfs` can then use the variables `visited` and `path` returned by the `find_path` function to continue.


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

`Coverage.py` was a new tool for us, but it was very well documented and easy to get into.
The installation process was super easy, and we never came across issues.
Using the `--help` flag provided sufficient information of how to use the tool.

### Your own coverage tool

Our coverage can be found [here](https://github.com/zsabbagh/algorithms/tree/1-coverage). We identified each branch, in each function, which are tagged with and incrementing ID starting at 1.
In `tests/__init__.py` we start writing to a data file.
We then run the unit tests, which calls the specific functions. If the functioncall enters a branch this information is saved. At the end of the function, we compile information about which branches were stepped into and the general coverage. If all branches are stepped into by a test the ID 0 is written to the branch-coverage file, since no branch has the ID of 0 the parser can interpret it as all branches covered and the number of columns remains the same.

To run the coverage tool manually on a function follow the steps.

1. create a data/branch-coverage file to store output (if it does not already exist)
2. Run unit tests which calls the specific function. For example, to run the branch coverage tool on `algorithms/matrix/sort_matrix_diagonally.py`:

```
python3 -m unit tests tests/test_matrix.py
cat data/branch-coverage
```

3. The tool will output information in the following format.
```
--- branch-coverage ---
function name,total branches,ratio,branches not covered
sort_matrix_diagonally,9,0.8888888888888888,1
```
This would correspond to one test function having branch coverage of 88%, with the identified branch not covered being ID:1.

Running all tests will write out several lines for example:

```
--- branch-coverage ---
function name,total branches,ratio,branches not covered
edmonds_karp,13,1.0,0
maximum_flow_bfs,11,1.0,
sort_matrix_diagonally,9,0.8888888888888888,1
knuth_morris_pratt,11,0.6363636363636364,3;5;7;9
knuth_morris_pratt,11,0.7272727272727273,3;4;7
knuth_morris_pratt,11,0.8181818181818182,3;10
knuth_morris_pratt,11,0.8181818181818182,3;5

```

4. ADD HOW THE PARSER PARSES AND OUTPUTS THIS INFO**
After running the unit tests for the functions with our own coverage tools, the file branch-coverage
gets populated with information. To get a JSON formatted result for each function,
run: `python3 scripts/branch_coverage_data_parser.py`.
Further, the `untested.py` script visualises, given a `Coverage.py` report, which
files are left untouched by the report.
In other words, it shows which *files* are covered by the unit tests.

### Evaluation

1. How detailed is your coverage measurement?
Our coverage tool only checks branch coverage. It does not check path coverage or unique paths taken through the branches.
Furthermore, in some instances as for `maximum_flow_bfs`, our coverage tool report 100% while the `coverage.py` tool does not.
This might indicate our tool is not as detailed in comparison.

2. What are the limitations of your own tool?

- One limitation of the tool is simple if statements in the code with no explicit else statements. Our tool would not recognize the alternative branch (corresponding to an else) if it does not explicitly exist. To solve this, we have manually added else statements.

- Another limitation is that the tool won't work on ternary operators.

- A third limitation which was discovered during the improvement of coverage, is early return statements. The tool writes the final report of covered branches in the end of the function right before a return. In `sort_matrix_diagonally.py` one branch (an if-statement) was included in the coverage report as missing. After adding a unit tests, this was still the case (using our own tool). This was due to the fact that the function returned immidiately if it stepped into the statement, thus never reporting/writing the coverage. To solve this we'd have to add the reporting before each return statement, or we would have to have to rewrite the function making sure that all returns are made after the coverage reporting.

3. Are the results of your tool consistent with existing coverage tools?

No, not neccesarily. Forexample, `sort_matrix_diagonally.py` has a coverage of 94% when checking the coverage report using coverage.py.

```
Name                                         Stmts Miss Branch BrPart  Cover Missing
algorithms/matrix/sort_matrix_diagonally.py   61    3     20      2    94%   33-34, 112
```
Our own tool, reported 88% from the ratio of 1/9, with only 9 branches identified. This points to the fact that `coverage.py` might be more finegrained.

## Coverage improvement

We actually worked with all 6 functions when checking the coverage, as several of these already had 100% branch coverage, in order for us to screen for appropriate functions to implement unit tests for.
What we ultimately found was the functions in the RBT class, together with
`sort_matrix_diagonally` and `knuth_morris_pratt` did not have 100% coverage.
In the case of RBT, the coverage was trivially improved by adding unit tests, since these did not exist.


Report of old coverage: [old_coverage.txt](https://github.com/zsabbagh/algorithms/blob/1-coverage/old_coverage.txt)

Report of new coverage: [new_coverage.txt](https://github.com/zsabbagh/algorithms/blob/3-new-tests/new_coverage.txt)

### Test cases added

**Glacier:**
- `sort_matrix_diagonally.py: test_sort_diagonally_with_vector`, a trivial test which checks the first identified branch. Specifically, if a matrix with 1 row or 1 column (vector) is provided as input, the entire vector should be returned as it is. The old branch coverage using coverage.py, was reported fass 94%. The new coverage was reported as 100%.

- `bellman_ford.py: test_bellman_ford_no_shortest_path` The `bellman_ford` function was not originally one of our chosen functions. However, due to many of them already having 100% branch coverage, this function was later retrieved with the sole purpose of improving branch coverage. The previous branch coverage was according to the general tool coverage.py report: 94%. There were no tests checking if there was no valid solution. The added test is therefore a graph with a negative cycle and should result in `false`. The function now has 100% branch coverage.
**Note: the function also has a high cyclomatic complexity of 8**

- **Additional note**: when looking for new functions, several function who reported not to have 100% branch coverage, acutally did. However, some of the related unit tests were residing in the same file, or was declared with non-unique names, causing some (or all) of the tests to never run during our procedures.

**Zakaria**
- `red_black_tree`, including `fix_insert` and `delete_fixup`, was previously 0% tested, with other words it did not even show up when the tests were run. Now the tests cover more than 70% of the entire code, i.e. all of the class methods.
- `red_black_tree` added tests to `minimum`, `maximum`, and `in_order` function.

**Einar**
- `knuth_morris_pratt` had 90% branch coverage, with one branch missing being tested. That branch was a while-loop within the making of the pi table. To enter the while-loop a specific condition must be met for the input pattern, there have to appear two identical letters in a row, followed by a letter that does not match. After creating the test case with the input parameter text being `aaaaaaa` and the pattern being `aabb` the test coverage increased to 100%.

- Since adding only one test meant it had full branch coverage, I began thinking about the path coverage.

  - I noticed there was not a single test where no letter from the pattern matched the text, so a test case for that was added. I also noticed there was not a test case where the text and pattern differ in data types. So I added a test case where the text is a list of integers and the pattern is a string. Those two are the first test cases where the first if-statement within the finding a pattern section is not entered.

  - I also noticed that there were no test cases where either the text or pattern (or both) were an empty string. This greatly alters the path taken since it affects if the for-loops are entered when making the pi table and finding a pattern.
    - Adding a test case where both are empty strings skips both loops.
    - If the text is an empty string but not the pattern, we only make the pi table but skip finding a pattern.
    - After adding a test case where the pattern is an empty string but not the text something interesting happened. The making of the pi table is skipped but within the for-loop for finding a pattern, an exception gets raised. That is because a letter from the text is compared to an indexed empty string.


## Self-assessment: Way of working

Current state according to the Essence standard:
We are in the "In Use" state. We are currently using our tools such as Github, Discord, Google Suite, lucid.app, to do our work and it has worked out fine so far. We have not inspected the tools in depth, and sometimes we've been using different tools for the same type of task which we've done in parallel. This has not been a problem. We do not have a specific procedures in place to handle feedback, so far we've simply discussed spontainously in discord if anyone has had any specific opinions on our way of working or anything else they'd like to share.

**Was the self-assessment unanimous? Any doubts about certain items?**

Yes, more or less.

**How have you improved so far?**
- Syncing more regarding distribution of workload/task assignment, to avoid accidently doing double work.
- Regarding syncing, we just now started collaborating through VS Code "Live Share". This enabled
the possibility to write on the report together.

**Where is potential for improvement?**

- We can probably we more rigorous in agreeing and picking one specific tool, and specific conventions if we would like a more uniform collection of work.

- We can do more pair-programming, working in groups/in person or make more use of live-share sessions.


## Overall experience

The key take-aways from this project is the idea of branch and code coverage.
It is immensely clever to be able to measure how *efficiently* the
crafted unit-tests actually covers and tests the written code.
It also provides certainty that the crafted tests are thought out
and has a purpose.
Quality is to be preferred when considering tests, not necessarily
quantity, since tests which monitors the same code and are
algorithmically identical does not ensure code quality.
