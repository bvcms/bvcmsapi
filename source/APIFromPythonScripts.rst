*todo*

Python Events
=============

These methods can be called as part of an event handler 
(e.g. run this when something happens like a registration, or a nightly batch).

Global Variables
-----------------

.. py:data:: model

    The object called ``model`` is how you access the following functions and properties of the **PythonEvents** class.
    
.. py:data:: DayOfWeek

    Readonly: Returns an integer number where:

    === ===
    Day returns
    === ===
    Sun 0
    Mon 1
    Tue 2
    Wed 3
    Thu 4
    Fri 5
    Sat 6
    === ===

.. py:data:: DateTime

    Readonly: The current day and time

.. py:data:: TestEmail

    ``model.TestEmail = true``
    causes all emails sent to during the script 
    to go to the currently logged in user's email.

.. py:data:: Transactional

    ``model.Transactional = true``
    Prevents sending notices about emails having been sent

Methods and Functions
----------------------

.. py:function:: CallScript(scriptName)

    Returns the output of the python script named ``scriptName`` as a string.
 
.. py:function:: EmailContent(savedQueryName, queuedById, fromEmail, fromName, contentName)
                 EmailContent(savedQueryName, queuedById, fromEmail, fromName, subject, contentName)
                 Email(savedQueryName, queuedById, fromEmail, fromName, subject, body)

    Sends an email a list of people from a saved query
    
    :param str savedQueryName: The name of the saved query that will specify the recipients.
    :param int queuedById:     The PeopleId of the coordinator's email address who is emailing on behalf of fromName
    :param str fromEmail:      The from email address
    :param str fromName:       The sender's name
    :param str subject:        The subject of the email (overrides the subject in the special content)
    :param str body:           The message content of the email.
    :param str contentName:    The name of the special content holding the message body and subject

.. py:function:: OrganizationIds(programId, divisionId)

    Returns a list of OrganizationIds in the respective program and division

    :param int programId:      The integer id number of the Program (use 0 for any program)
    :param int divisionId:     The integer id of the Division (use 0 for any division)

.. py:function:: OrgMembersQuery(programId, divisionId, organizationId, memberTypes)

    This method will return an id that can be used in the following Email2 function

    :param int programId:      The integer id number of the Program (use 0 for any program)
    :param int divisionId:     The integer id of the Division (use 0 for any division)
    :param int organizationId: The integer id of the Organization (use 0 for any organization)
    :param str memberTypes:    A comma separated string---with no spaces around the commas---of 
                               exact MemberType descriptions used to filter just members with one of those types.


.. py:function:: Email2(id, queuedById, fromEmail, fromName, subject, body)

    Sends an email to a list of organization members.

    :param int id:             The identifier returned by the ``OrgMembersQuery`` function above
    :param int queuedById:     The PeopleId of the coordinator's email address who is emailing on behalf of *fromName*
    :param str fromEmail:      The from email address
    :param str fromName:       The sender's name
    :param str subject:        The subject of the email (overrides the subject in the special content)
    :param str body:           The message content of the email.


Add / Edit Extra Values
-------------------------

The following methods will update or add values to everybody in the
results set of the specified saved query

.. py:function:: AddExtraValueCode(savedQueryName, name, code)
                 AddExtraValueCode(peopleId, name, code)

    :param str savedQueryName: The name of the saved query defining the list of people to update
    :param int peopleId:       The peopleId of the individual person to update
    :param str name:           The name of the Extra Value Field
    :param str code:           The code value (text)

.. py:function:: AddExtraValueText(savedQueryName, name, text)
                 AddExtraValueText(peopleId, name, text)

    :param str savedQueryName: The name of the saved query defining the list of people to update
    :param int peopleId:       The peopleId of the individual person to update
    :param str name:           The name of the Extra Value Field
    :param str text:           The text value

.. py:function:: AddExtraValueDate(savedQueryName, name, date)
                 AddExtraValueDate(peopleId, name, date)

    :param str savedQueryName: The name of the saved query defining the list of people to update
    :param int peopleId:       The peopleId of the individual person to update
    :param str name:           The name of the Extra Value Field
    :param date date:          The date value

.. py:function:: AddExtraValueInt(savedQueryName, name, number)
                 AddExtraValueInt(peopleId, name, number)

    :param str savedQueryName: The name of the saved query defining the list of people to update
    :param int peopleId:       The peopleId of the individual person to update
    :param str name:           The name of the Extra Value Field
    :param str number:         The integer value (not in quotes)

.. py:function:: AddExtraValueBool(savedQueryName, name, truefalse)
                 AddExtraValueBool(peopleId, name, truefalse)

    :param str savedQueryName: The name of the saved query defining the list of people to update
    :param int peopleId:       The peopleId of the individual person to update
    :param str name:           The name of the Extra Value Field
    :param bool truefalse:     The boolean value (true or false)

.. py:function:: UpdateCampus(savedQueryName, campusName)
                 UpdateCampus(peopleId, campusName)

    :param str savedQueryName: The name of the saved query defining the list of people to update
    :param int peopleId:       The peopleId of the individual person to update
    :param str campusName:     The campus name (use exact spelling to match an existing campus)

.. py:function:: UpdateMemberStatus(savedQueryName, statusName)
                 UpdateMemberStatus(peopleId, statusName)

    :param str savedQueryName: The name of the saved query defining the list of people to update
    :param int peopleId:       The peopleId of the individual person to update
    :param str status:         The status description (use exact spelling to match existing status)

.. py:function:: UpdateNewMemberClassStatus(savedQueryName, statusName)
                 UpdateNewMemberClassStatus(peopleId, statusName)

    :param str savedQueryName: The name of the saved query defining the list of people to update
    :param int peopleId:       The peopleId of the individual person to update
    :param str status:         The status description (use exact spelling to match existing status)

.. py:function:: UpdateNewMemberClassDate(savedQueryName, date)
                 UpdateNewMemberClassDate(peopleId, date)

    :param str savedQueryName: The name of the saved query defining the list of people to update
    :param int peopleId:       The peopleId of the individual person to update
    :param str date:           The date value

.. py:function:: AddMembersToOrg(savedQueryName, organizationId)
                 AddMemberToOrg(peopleId, organizationId)

    :param str savedQueryName: The name of the saved query defining the list of people to update
    :param int peopleId:       The peopleId of the individual person to update
    :param int organizationId: The organizationId number to add the person too

Fetch Extra Values
-------------------------

The following functions will return extra values for a person

.. py:function:: ExtraValueCode(peopleId, name)
                 ExtraValueText(peopleId, name)
                 ExtraValueInt(peopleId, name)
                 ExtraValueDate(peopleId, name)
                 ExtraValueBit(peopleId, name)

    Returns the code,text,int,datetime,boolean value for the indicated person

    :param int peopleId:       The peopleId of the person
    :param str name:           The name of the Extra Value Field

