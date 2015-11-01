FPU Packet Pickup Form
======================

Below is the form used for the FPUPacketPickup sample project. 
This was built with `bootsnipp form builder <http://bootsnipp.com/forms>`_.

Note the highlighted lines where changes were made to the bootsnipp generated html.

On line 63 an 66, you will see `{{pyscript}}` and `{{wandtarget}}`. 
These will be replaced with the name of the Python script file 
and the resulting of the wandtarget textbox when the form is posted. 
The double curly braces are know as handlebar notations (think of a bicycle handle bar). 
Handlebars is the library we use to replace values for HTML content. 
The `model.Data` is an object to which these values are assigned.
Any form elements that are posted using a submit button on the page 
will be available in the `model.Data` object in addition to anything else you assign to that object.

* `model.Data.pyscript` is set internally to the name of the Python Script file.
* `model.Data.wandtarget` is set when the form is posted by the user.

.. literalinclude:: FPUPacketForm.html
  :language: html
  :linenos:
  :emphasize-lines: 63,66,71-74

Lines 71-74 contain the div which will be used to display any messages you return using the `print` statement. 
It must have an id of "output" for this to work.

Section to be added:

.. code-block:: html
  
    <!-- Notice Area -->
    <div class="form-group">
      <div id="output" class="col-md-4 col-md-offset-4"></div>
    </div>


