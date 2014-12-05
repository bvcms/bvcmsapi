*todo*

API OneTimeLoginLink
====================

**NOTE: Because this is outside the scope of our support team and
requires the developer to provide support, we do not have the resources
to do this without asking for additional fees. Therefore, in order to
use the API, you must either be a sponsoring church or pay an additional
fee. **

If you want to have your users login to your external Church Web Site,
you can authenticate their credentials against BVCMS. This can return
you interesting information regarding this person.

Once a user is validated, you can allow them to interact with pages on
BVCMS as if they had logged in there normally. This works with both the
standard site and with registrations.

Given two sites, the Church Web Site (Site A) and BVCMS (Site B), here
is the flow:

#. User logs into Site A
#. Site A validates the username / password against the Login API on
   Site B
#. Interesting information about the person is returned in XML for Site
   A to use
#. User interacts with Site A doing things that Site A allows an
   authorized user
#. Site A presents to the User a link to visit Site B
#. User clicks this link
#. Site A receives the request and processes it by requesting a
   OneTimeLoginLink from Site B

   -  The first method below is for online registrations
   -  The second method is for any other URL on Site B
   -  Neither return the domain part (https://church.bvcms.com/)

#. Site A redirects user to the Login page of Site B with both a desired
   URL and a OneTimeLogin token as parameters
#. Site B sees the OneTimeLogin parameter and validates it, and
   discovers the user's identity in the process
#. Site B then does not require any user interaction and redirects the
   User to the desired page with the user fully authenticated
#. Site B then marks the OneTimeLink as used so that it cannot be used
   again.

::

::

            [HttpPost]
            [RequireBasicAuthentication]
            public ActionResult GetOneTimeRegisterLink(int PeopleId, int OrgId)

::

            [HttpPost]
            [RequireBasicAuthentication]
            public ActionResult GetOneTimeLoginLink(string url, string user)


