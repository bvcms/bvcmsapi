FPU Packet Pickup Javascript
============================

Return to :doc:`index`.

Below is the javascript used for the FPUPacketPickup sample project
with some high level explanation following:

.. literalinclude:: FPUPacket.js
  :language: javascript
  :linenos:

Lines 6 and 8
        Pressing Enter or clicking Action will start the action() to act on the barcode.

Lines 15-19
        If there is a barcode already there, 
        then erase it first so that the form is ready to scan the next barcode.

Lines 20-24
        Send the form inputs via POST method to the script on the server.

Lines 26-35
        Reset the form to the default values when the "Clear" button is clicked.
