FPU Packet Pickup Process
=========================

Return to :doc:`index`.

When someone scans the barcode or clicks the action button,
the following Pytyon script is run to process the results.
An explanation follows the script.

.. literalinclude:: FPUPacketProcess.py
  :language: python
  :linenos:

Explanation of code
^^^^^^^^^^^^^^^^^^^^^

The entire script consists of the defination of a function called Process() 
followed by a call to that function. 
The reason a function is defined, is to make it easy to return from the script at various points in the process
which also keeps from having to nest the code in more if statements.

Line 2
        This line checks to see if there is a barcode that has been entered or scanned and returns, doing nothing if not.

Lines 5-7
        Decomposes the barcode into the two consituant parts, 
        orgid and peopleid.

Lines 9-14
        Gets the person, spouse and class (the organization)
        for the registrant using built in functions 
        available to TouchPoint's Python scripts.
        The InOrg function returns true or false 
        whether a person is a member of the org or not.

Lines 16-23 
        Display various warning messages for missing or incorrect data.

Line 25
        Begins the rest of the process if the person and org exist.

Line 26-41
        Displays a table with information about the registration.
        Line 34 returns if the person is not a member of the org.

Lines 43-55
        Adds or removes a person from the "pay online" sub-group 
        based on the first two radio buttons checked.

        The default Paid option button is "no change" (line 49)
        and will display the paid status for the user.

Lines 57-59
        If the radio button for "Mark Not Picked up" is checked,
        then the person is removed from the "packet-pickedup" sub-group.

Lines 60-67
        The default for the this radio button group ("Picked up")
        is to mark the person has having picked up their packet.
        These if, elif, else statements 
        will indicate whether the Packet has already been picked up,
        or whether the Packet has not been successfully marked as picked up.

Line 69
        Finally, the actual work does not happen 
        until the Process() function, just defined, is called.


The FPUPacket.js file will post the form to the script and the script FPUPacketProcess.py will be called.

.. code-block:: javascript
        
        $.post("/PyScriptForm/", q, function (ret) {
            $("#output").html(ret);
            $("#wandtarget").focus();
        });

