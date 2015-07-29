Python Events
=============

These methods can be called as part of an event handler 
(e.g. run this when something happens like a registration, or a nightly batch).

Global Variables
-----------------

.. py:data:: model

    The object called ``model`` is how you access the following functions and properties of the **PythonEvents** class.
    
.. py:data:: DayOfWeek

    :return: the day of the week represented by a number (``0-6``) 0=Sunday
    :rtype: int

.. py:data:: DateTime

    :return: The current day and time (readonly)
    :rtype: datetime

.. py:data:: TestEmail

    :rtype: boolean

    The following causes all emails sent to during the script
    to go to the currently logged in user's email.::

        model.TestEmail = True

.. py:data:: Transactional

    Prevents sending notices about emails having been sent::

        model.Transactional = True

Used By PyScriptForm
~~~~~~~~~~~~~~~~~~~~~

These are all available as properties on the model

.. py:data:: Form

    :rtype: string

    Set this to the HTML you wish to display as a form on your page.
    It is loaded into your page by the /PyScriptForm/*YourScript* GET method.

.. py:data:: Script

    :rtype: string

    Set this to the Javascript you want to run on your page.
    It is loaded into your page by the /PyScriptForm/*YourScript* GET method.

.. py:data:: Header

    :rtype: string

    Set this to the title of your page

.. py:data:: HttpMethod

    :return: Either 'get' or 'post'
    :rtype: string

    This method let's you determine action based on whether it is the initial page load (get)
    or the ajax postback from your Javascript (post)

Methods and Functions
----------------------

.. py:function:: CallScript(scriptName)

    :param str scriptName: The name of the Python Script Special Content
    :return: the output of the script as if you had used a ``print`` statement

.. py:function:: EmailContent(savedQueryName, queuedById, fromEmail, fromName, contentName)
                 EmailContent2(savedQueryName, queuedById, fromEmail, fromName, subject, contentName)
                 Email(savedQueryName, queuedById, fromEmail, fromName, subject, body)

    Sends an email to a list of people from a saved query
    
    :param str savedQueryName: The name of the saved query that will specify the recipients.
    :param int queuedById:     The PeopleId of the coordinator's email address who is emailing on behalf of fromName
    :param str fromEmail:      The from email address
    :param str fromName:       The sender's name
    :param str subject:        The subject of the email (overrides the subject in the special content)
    :param str body:           The message content of the email.
    :param str contentName:    The name of the special content holding the message body and subject

.. py:function:: PeopleIds(savedQueryName)

    :return: a list of PeopleIds from a query
    :param str savedQueryName: The name of the saved query that will specify the recipients.

    Example::

        pids = model.PeopleIds("savedquery")
        for pid in pids:
            p = model.GetPerson(pid)
            print p.Name

.. py:function:: OrganizationIds(programId, divisionId)

    :return: a list of OrganizationIds in the respective program and division
    :param int programId:      The integer id number of the Program (use 0 for any program)
    :param int divisionId:     The integer id of the Division (use 0 for any division)

.. py:function:: OrgMembersQuery(programId, divisionId, organizationId, memberTypes)

    :return: an id that can be used in the following ``Email2`` function
    :rtype: int
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

.. py:function:: UpdateNewMemberClassDateIfNullForLastAttended(savedQueryName, orgId)
                 UpdateNewMemberClassDateIfNullForLastAttended(peopleId, orgId)

    :param str savedQueryName: The name of the saved query defining the list of people to update
    :param int peopleId:       The peopleId of the individual person to update
    :param str orgId:          The organization ID for the last attend meeting

.. py:function:: AddMembersToOrg(savedQueryName, organizationId)
                 AddMemberToOrg(peopleId, organizationId)

    :param str savedQueryName: The name of the saved query defining the list of people to update
    :param int peopleId:       The peopleId of the individual person to update
    :param int organizationId: The organizationId number to add the person too


.. py:function:: InOrg(pid, OrgId)

    Determines whether a person is a member of an organization.

    :rtype: boolean
    :param int pid:     PeopleId
    :param int OrgId:   OrganizationId

.. py:function:: AddSubGroup(pid, OrgId, group)

    Adds a person to a sub-group in the organization.

    :param int pid:     PeopleId
    :param int OrgId:   OrganizationId
    :param str group:   The name of the sub-group

.. py:function:: RemoveSubGroup(pid, OrgId, group)

    Removes a person from a sub-group in the organization.

    :param int pid:     PeopleId
    :param int OrgId:   OrganizationId
    :param str group:   The name of the sub-group

.. py:function:: FmtPhone(phone, prefix)

    :param str phone:   The phone number of the sub-group
    :param str prefix:  Goes in front of the formatted number.  e.g. (c) for cell phone

.. py:function:: InSubGroup(pid, OrgId, group)

    Determines whether a person is in a sub-group in organization

    :rtype: boolean
    :param int pid:     PeopleId
    :param int OrgId:   OrganizationId
    :param str group:   The name of the sub-group

Fetch Extra Values
-------------------------

The following functions will return extra values for a person

.. py:function:: ExtraValueCode(peopleId, name)
                 ExtraValueText(peopleId, name)
                 ExtraValueInt(peopleId, name)
                 ExtraValueDate(peopleId, name)
                 ExtraValueBit(peopleId, name)

    :return: the code, text, int, datetime, boolean value for the indicated person
    :rtype: Code and Text returns string, others return native type (int, datetime, bool)
    :param int peopleId:       The peopleId of the person
    :param str name:           The name of the Extra Value Field


Person Object
-------------

.. py:function:: GetPerson(peopleid)

    :return: object having all the fields about a person
    :rtype: see Person object definition below

    .. py:class:: Address

        ========= =====================
        string    **AddressLineOne**
        string    **AddressLineTwo**
        string    **CityName**
        string    **StateCode**
        string    **ZipCode**
        string    **CountryName**
        DateTime? **AddressFromDate**
        DateTime? **AddressToDate**
        bool?     **BadAddressFlag**
        ========= =====================

    .. py:class:: Person

        =========== =====================
        int         **PeopleId**
        int         **FamilyId**
        string      **NickName**
        string      **TitleCode**
        string      **FirstName**
        string      **MiddleName**
        string      **LastName**
        string      **Name**
        string      **SuffixCode**
        string      **AltName**
        string      **MaidenName**
        string      **HomePhone**
        string      **CellPhone**
        string      **WorkPhone**
        string      **EmailAddress**
        bool?       **SendEmailAddress1**
        string      **EmailAddress2**
        bool?       **SendEmailAddress2**
        string      **SchoolOther**
        int?        **Grade**
        string      **EmployerOther**
        string      **OccupationOther**
        int?        **MaritalStatusId**
        DateTime?   **WeddingDate**
        string      **DOB**
        bool?       **DoNotCallFlag**
        bool?       **DoNotMailFlag**
        bool?       **DoNotVisitFlag**
        int         **PositionInFamilyId**
        string      **SpouseName**
        int?        **CampusId**
        DateTime?   **DeceasedDate**
        int?        **MemberStatusId**
        DateTime?   **JoinDate**
        int?        **DecisionTypeId**
        DateTime?   **DecisionDate**
        int?        **BaptismTypeId**
        DateTime?   **BaptismDate**
        DateTime?   **BaptismSchedDate**
        string      **OtherPreviousChurch**
        int?        **JoinCodeId**
        int?        **DropCodeId**
        DateTime?   **DropDate**
        string      **OtherNewChurch**
        string      **EmContact**
        string      **EmPhone**
        int?        **NewMemberClassStatusId**
        DateTime?   **NewMemberClassDate**
        Address     **FamilyAddress**
        Address     **PersonalAddress**
        int         **AddressTypeId**
        string[]    **Usernames**
        =========== =====================

Organization Object
--------------------

.. py:function:: GetOrganization(OrgId)

    :return:    object having all the fields about a person
    :rtype:     Organization (see Organization object definition below)

    .. py:class:: Organization

        =========== =====================
        int         **id**
        string      **name**
        string      **location**
        string      **description**
        =========== =====================

