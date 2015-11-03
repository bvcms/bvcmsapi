FPU Packet Pickup Confirmation
===============================

Return to :doc:`index`.

Below is the HTML used as a confirmation email for a registrant 
of a Financial Peace University class. 
The email indicates that it is important to bring the confirmation 
with the barcode to pick up their packet.

Line 10 shows the email replacement code for a barcode
that will contain the orgid and the peopleid formatted as `33-444`,
where 33 is the orgid and 444 is the peopleid. 
That format is used by the Python FPUPacketProcess.py script 
to take action on this person in this class.

.. note::
        This content should be part of your `Registration > Messages > Confirmation`
        in your registration Organizations.

.. literalinclude:: Files/FPUPacketConfirmation.html
  :language: html
  :linenos:
  :emphasize-lines: 10

