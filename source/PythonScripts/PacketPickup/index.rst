Financial Peace University Packet Pickup Project
================================================

Here are the various components of this project:

* :doc:`entrypoint`
* :doc:`form`
* :doc:`javascript`
* :doc:`process`
* :doc:`confirmation`

Overview
^^^^^^^^

We are documenting this process because we know that other churches may
have similar needs and be interested in using it.
They may be intrigued to see how TouchPoint can be extended
through the use of Python Scripts while making it appear as an integral part of TouchPoint.

This is the page you use to record a packet is picked up.

.. figure:: http://i.bvcms.com/2015-11-03_10-52-13.png
    :target: #

    Packet Pickup Page


We implemented this project here at Bellevue Baptist Church.
We were hosting about 80 classes, meeting every day of the week with multiple schedules,
and three different start dates.
The idea was that we would get everybody at our church signed up for these classes, 
and invite many from outside the church as well.
This means that we registered more than 1,000 people using the TouchPoint system.

Part of the signup process involved allowing 
a registrant to choose to purchase a packet (one per couple),
or indicate that they already had a packet because they had already attended FPU previously.
The packets could be picked up starting a few days before the first class 
and would continue for several weeks during the various start dates for individual classes.

Because the packets are expensive ($80) we needed a good accounting of when a person picked up the packet.
Further complicating matters is the fact that the packet could be picked up by either the husband or the wife.
Because couples would share the packet, 
both husband and wife would need to be marked as having paid and picked-up 
if only one of them had picked up their packet.

Also, we needed a way to verify that they had indeed already paid for a packet,
either at the pickup desk or during the online registration.

The registrant would receive an email confirmation containing a bar-code embedded with their class and peopleid.
This confirmation could either be printed or presented electronically on their smart-phone.
Then we would scan their barcode when they picked up their packet.
