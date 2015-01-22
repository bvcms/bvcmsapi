form-ajax.js usage
===================

The form-ajax.js code is used to bind post-back / refresh calls for the following:

- forms
- paged tables
- modal dialogs
- just-in-time tab population

These are common patterns within bvcms.
For paging, sorting and pagesize on table views,
form-ajax works in concert with the ``PagedTableModel`` class in bvcms. 


How postback/refresh events are triggered
-------------------------------------------

Any anchor tag can trigger a postback.
Both the enclsing form and the anchor tag itself must have a class of ``ajax``.

An enclosing form is not requred if the anchor is part of a bootstrap ``ul.nav-tabs`` construct.
In this case, the form targeted will be the identified form descendant of the div.tab-pane pointed to by the clicked link's href value.
This tab-pane div is what is used to hold the tab's contents.

URL view target links
----------------------

Every round trip  the form-ajax code will make to the server
will post data in the form and use the returned html to render the form again.
The URL that is called is taking from one of the following places, in order,
using the first non null value.

- passing the URL directly to the ``$.formAjaxClick(ele, link)`` call via the link argument.
- a data-link attribute on the element triggering the event.
- the data-link attribute on closest enclosing form
  
