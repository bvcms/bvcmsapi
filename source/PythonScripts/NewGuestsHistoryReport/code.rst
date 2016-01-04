Explanation of the code in the script
======================================
For the New Guest History Report
------------------------------------

The following is the SearchBuilder code template
that is used to build the counts for each row and column.
This code has three placeholders (the empty braces ``{}`` ).
These will be replaced with the appropriate division id 
and start/end dates for the query. 
In the current form, with the placeholders, 
it is in essence a template and is not executable yet.

.. literalinclude:: Files/NewGuestHistory.py
        :lines: 4-7
        :lineno-start: 4
        :linenos:

.. note::
        In python, a string of characters 
        is quoted with single quotes or double quotes like so::
       
                str = 'a string' 
                str = "a string"

        But multi-line strings are quoted with triple quotes.
                
We use a statement like ``query2 = query.format(123, '7/1/14', '7/1/15')``
to convert this query into a string that is executable. 
This statement will result in a query like the following.
You can see how the placeholders ``{}`` have been replaced.

        AttendTypeAsOf( Prog=101[Life Groups], Div=123, StartDate='7/1/14', EndDate='7/1/15' ) = 60[New Guest]
        AND IncludeDeceased = 1[True]


The following code builds a list of dates that will represent 
the starting dates for each column of counts in the results.

.. literalinclude:: Files/NewGuestHistory.py
        :lines: 9-19
        :lineno-start: 9
        :linenos:

The next list is each row representing a division of
of Sunday School classes within the Life Groups program.

.. literalinclude:: Files/newguesthistory.py
        :lines: 21-38
        :lineno-start: 21
        :linenos:

.. note::
        You can get a list of divisions in your own database 
        by going to `Admin > Divisions > Codes`.

        The division id is the number 
        and the text in brackets is the name of the division. 
        The names will be used to display on each row.

This code declares a class called Row 
that will be used to hold the data in the Rows and Columns in the report.
Each Row has a name and a list of columns. 

.. literalinclude:: Files/NewGuestHistory.py
        :lines: 40-43
        :lineno-start: 40
        :linenos:

.. seealso:: `www.jeffknupp.com <http://www.jeffknupp.com/blog/2014/06/18/improve-your-python-python-classes-and-object-oriented-programming/>`_ or the 
        `official Python docs <https://docs.python.org/2/tutorial/classes.html>`_
        for more information about objects and classes in Python.

The following code creates and initializes the header row 
and the footer row for the results.
An instance of a Row is constructed with a statement like those on lines 48 and 49.
Lines 52-54 initialie the ``cols`` list in the Row object. 
There are as many columns as there are dates 
so we loop through the list of dates to make the assignments.

.. literalinclude:: Files/NewGuestHistory.py
        :lines: 45-54
        :lineno-start: 45
        :linenos:

.. note::
        The Data object is a built-in object that can hold anything.
        It will be used when rendering the table in the last step.


The next section of code loops through the list of divisions 
and builds/runs the query needed for each column of each row/division. 

58. The name of the division is parsed from this pattern: ``123[this is the name]`` 
    out of the division list using ``split`` and ``strip`` Python functions.
59. Each division gets it own row object
60. Then we have another date loop for each column in the row.
61. The enddt is computed from the startdt using the DateAddDays function 
    which is available in the model used to execute your script.
62. The specific query needed for this division 
    and date range is built from the template query, 
    and placed into the ``rowcolquery`` variable.
63. The ready-to-execute query string is used by 
    the ``q.QueryCodeCount(rowcolquery)`` function call 
    which returns the count of people who satisfy the conditions of the query.
64. The ``len`` function returns the current length of the list
    and we use that to get the correct column in the footer row.
65. The footer is updated with the new total for that date's column.
66. The new column for that row is added to the list of cols.
67. Finally, now that all the dates/columns are done for the Row, 
    the row for this division is added to the list of rows.
 
.. literalinclude:: Files/NewGuestHistory.py
        :lines: 56-67
        :lineno-start: 56
        :linenos:

This next code is the template which will be used to render the final report.
This type of template is called a *HandleBars* template 
because of the use of double sets of curly braces ``{{}}``
(they look like bicycle handle bars). 
This template is a multi-line string stored in a variable called template 
which will be used in the last statement to render the report.

Each use of the handlebars is documented. The HTML used will not be documented.

74. This will replace the handlebars with the value 
    of the header Row object's name attribute.
    
75. The ``{{#each header.cols}}`` begins a loop 
    iterating over each column in the cols list on the header Row object.

76. The ``this`` keyword is the current value in the iteration in the loop, 
    a date string in this case.

77. The ``{{/each}}`` marks the end of the loop.

81. This begins the loop over each row in the rows list 
    (which we created as an object on the built-in Data object).

83. The name of the current Row object (row) is displayed here.

84. For this row, we need to comlete the row by 
    iterating over each col in the row's cols list.

85. We use a special ``Fmt`` helper available in the BVCMS implementation of handlebars.
    The ``this`` keyword is the 
    value of the current item in the cols list of the row being worked on.
    The ``"N0"`` is a formating string indicating that 
    we want to display an integer number with no decimal places.
    The displayed number will be displayed with commas if greater than 999.

86. Indicate the end of the loop through each of the cols.

87. Indicate the end of the loop through each the rows.

92. Line numbers 92-95 work the same as each division row, but for the footer object.

.. literalinclude:: Files/NewGuestHistory.py
        :lines: 69-99
        :lineno-start: 69
        :linenos:

Finally, the table of results 
is printed on the page using the ``RenderTemplate`` function of BVCMS Python model.

.. literalinclude:: Files/NewGuestHistory.py
        :lines: 101
        :lineno-start: 101
        :linenos:

.. seealso:: The whole script: :doc:`script`
