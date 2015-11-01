FPU Packet Pickup Confirmation
===============================

Below is the HTML used as a confirmation email for a registrant 
of a Financial Peace University class. 
The email indicates that it is important to bring the confirmation 
with the barcode to pick up their packet.

Note line 10 showing the email replacement code for a barcode 
that will contain the orgid and the peopleid in formatted as 33-444 
where 33 is the orgid and 444 is the peopleid. 
That format is used by the Python FPUPacketProcess.py script 
to take action on this person in this class.

.. literalinclude:: FPUPacketConfirmation.html
  :language: html
  :linenos:
  :emphasize-lines: 10

return to :doc:`index`
