FPU Packet Pickup Main Script
==============================

Return to :doc:`index`.

Below is the main Python script used for the FPUPacketPickup sample project
with explanation following.

.. note::
        This file should be located under 
        `Admin > Special Content > PythonScripts` tab, and be named `FPUPacket`.
        It goes under this tab because it can be run directly from the editor
        which will show you the URL to launch it for your users.

.. literalinclude:: Files/FPUPacket.py
  :language: python
  :linenos:

This script is short but is responsible for routing the process.
The `model.HttpMethod` indicates the page was called.

Line 1-4
        A `model.HttpMethod` with a value of `get` 
        will cause the form to display initially.
        First, the html contents are retrieved from `FPUPacketForm.html` 
        and then rendered into the `model.Form` global variable.
        `model.Form` is used to display the form on the page.
        Second the javascript is retrieved from the `FPUPacket.js` content
        and is also rendered on the page.

        .. seealso::
                :doc:`form`

Lines 6-7
        If `model.HttpMethod` is `post`, that means
        that a button click or some other action was taken by the user.
        The rest of the process is routed to the `FPUPacketProcess.py` script.

        .. seealso::
                :doc:`process`


