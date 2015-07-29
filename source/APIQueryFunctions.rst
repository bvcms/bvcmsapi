Query Functions
================

These methods can be called as part of an event handler 
(e.g. run this when something happens like a registration, or a nightly batch).

Global Variables
-----------------

.. py:data:: LastSunday

    :return: The the most recent Sunday prior to today on which there are meetings with recorded attendance
    :rtype: datetime

Methods and Functions
----------------------

.. py:function:: AttendCountAsOf(startdt, enddt, guestonly, progid, divid, orgid)
		 AttendMemberTypeCountAsOf(startdt, enddt, membertypes, notmembertypes, progid, divid, orgid)

    :rtype: int
    :param date startdt:
    :param date enddt:
    :param bool guestonly:
    :param str membertypes:
    :param str notmembertypes:
    :param int progid:
    :param int divid:
    :param int orgid:

.. py:function:: AttendanceTypeCountDateRange(progid, divid, orgid, attendtype, startdt, days)

    :rtype: int
    :param int progid:
    :param int divid:
    :param int orgid:
    :param str attendtype:
    :param date startdt:
    :param int days:
        
.. py:function:: ContributionTotals(days1, days2, fundid)

    :rtype: float
    :param int days1:
    :param int days2:
    :param int fundid:

.. py:function:: ContributionCount2(days1, days2, fundid)

    :rtype: int
    :param int days1:
    :param int days2:
    :param int fundid:

.. py:function:: ContributionCount(days, fundid)

    :rtype: int
    :param int days:
    :param int fundid:
        
.. py:function:: ContributionTotals(days1, days2, funds)

    :rtype: float
    :param int days1:
    :param int days2:
    :param str funds:

.. py:function:: ContributionCount(days1, days2, funds)

    :rtype: int
    :param int days1:
    :param int days2:
    :param str funds:

.. py:function:: ContributionCount(days, funds)

    :rtype: int
    :param int days:
    :param str funds:

.. py:function:: DecisionCountDateRange(decisiontype, startdt, days)

    :rtype: int
    :param str decisiontype:
    :param date startdt:
    :param int days:
        
.. py:function:: LastWeekAttendance(progid, divid, starthour, endhour)

    :rtype: int
    :param int progid:
    :param int divid:
    :param int starthour:
    :param int endhour:

.. py:function:: MeetingCountDateHours(progid, divid, orgid, startdt, hours)

    :rtype: int
    :param int progid:
    :param int divid:
    :param int orgid:
    :param date startdt:
    :param int hours:
        
.. py:function:: MeetingCount(days, progid, divid, orgid)

    :rtype: int
    :param int days:
    :param int progid:
    :param int divid:
    :param int orgid:

.. py:function:: NumPresent(days, progid, divid, orgid)

    :rtype: int
    :param int days:
    :param int progid:
    :param int divid:
    :param int orgid:
        
.. py:function:: NumPresentDateRange(progid, divid, orgid, startdt, days)

    :rtype: int
    :param int progid:
    :param int divid:
    :param int orgid:
    :param date startdt:
    :param int days:

.. py:function:: QueryCount(savedQuery)

    :rtype: int
    :param str savedQuery:

.. py:function:: QueryCountDivDateRange(savedQuery, division, startdt, days)

    :rtype: int
    :param str savedQuery:
        
.. py:function:: QueryCountProgIdDivDateRange(savedQuery, progid, division, startdt, days)

    :rtype: int

.. py:function:: QueryCountDivDate(savedQuery, division, startdt)

    :rtype: int
        
.. py:function:: QueryCountDivDate(savedQuery, progid, division, startdt)

    :rtype: int
        
.. py:function:: QueryCountDateRange(savedQuery, startdt, days)

    :rtype: int
        
.. py:function:: QueryCountDate(savedQuery, startdt)

    :rtype: int
        
.. py:function:: QueryList(savedQuery)
                 QueryList2(savedQuery, orderByParam, ascending)

    :return: An enumerable list of Person objects up to a maximum of 1,000
    :param str savedQuery:   The name of the savedQuery to execute
    :param str orderByParam: The name of the column to sort by (age, birthday, or name)
    :param bool ascending:   true = ascending, false = descending

.. py:function:: RegistrationCount(days, progid, divid, orgid)

    :rtype: int
        
.. py:function:: SqlNameCountArray(title, sql)

    :rtype: str
        
.. py:function:: StatusCount(s)

    :rtype: int


