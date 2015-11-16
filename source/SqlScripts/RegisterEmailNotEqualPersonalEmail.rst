Register Email not Equal to Personal Email
==========================================

Using the script below,
you can create a Sql script
that, when run,
will display a report of everyone who has
registered online and used an email address
that is different from the one on their personal record.

Information Displayed
    - Name is the registrant's name.
    - RegisterEmail is the email entered during registration.
    - EmailAddress is the Primary Email on the person's record.
    - EmailAddress2 is the Secondary Email on the person's record.
    - OrganizationName is the name of the organization in which the person registered.
    - PeopleId is a link to the person's record.
    - OrganizationId is the Org ID for the registration organization.

Using this report, you can click the person's PID# link
and then click the MemberType for the registration organization
and view the registration email.

You can remove it, if necessary, by clicking Edit
in the Member Dialog.

Create Sql Script
-----------------

Step 1
    Go to `Administration > Setup > Special Content`
    and select the `Sql Scripts` tab.

Step 2
    Click the green `+New Sql Script File` button.
    Enter the name exaclty in this format -
    ``RegisterEmailNotEqualPersonalEmail``
    and `Submit`.

Step 3
    Copy the script below and paste into
    the Sql Script you just created,
    and `Save Sql Script`.

Now you can click `Run Script` and bookmark the page
for future use.

If you prefer an Excel version,
check `Excel Output?` and then `Run Script`.

.. code-block:: sql

    SELECT
	p.Name2,
	m.RegisterEmail,
	p.EmailAddress,
	ISNULL(p.EmailAddress2, '') EmailAddress2,
	o.OrganizationName,
	p.PeopleId,
	o.OrganizationId
    FROM dbo.OrganizationMembers m
    JOIN dbo.Organizations o ON o.OrganizationId = m.OrganizationId
    JOIN dbo.People p ON p.PeopleId = m.PeopleId
    WHERE RegisterEmail LIKE '%@%' AND m.RegisterEmail <> p.EmailAddress
    ORDER BY p.Name2, p.PeopleId, o.OrganizationName