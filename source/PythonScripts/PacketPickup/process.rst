FPU Packet Pickup Process
=========================

When someone scans the barcode or clicks the action button,
the following Pytyon script is run to process the results.

The FPUPacket.js file will post the form to the script and the script FPUPacketProcess.py will be called.



* `model.Data.pyscript` is set internally to the name of the Python Script file.
* `model.Data.wandtarget` is set when the form is posted by the user.

.. literalinclude:: FPUPacketProcess.py
  :language: python
  :linenos:

return to :doc:`index`
