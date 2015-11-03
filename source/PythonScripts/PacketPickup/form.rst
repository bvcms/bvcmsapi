
FPU Packet Pickup Form
======================

Return to :doc:`index`.

Below is the form used for the FPUPacketPickup sample project. 
This was built with `bootsnipp form builder <http://bootsnipp.com/forms>`_.
Following the form is an explanation of important items to note.

.. note::
        This file should be located under 
        `Admin > Special Content > Text` tab, and be named `FPUPacketForm.html`.
        It goes under the Text tab because, 
        the HTML tab uses a special editor 
        which will reformat your document and could cause problems.
        The text tab will remain intact---however you create and format your document.

.. literalinclude:: Files/FPUPacketForm.html
  :language: html
  :linenos:
  :emphasize-lines: 63,66,71-74

Lines 12, 18, 24
        When using bootsnipp to build this form, 
        pay close attention to the name and id for these various input elements
        for the Pay Options radio buttons.
        The name of all three radio buttons is `paidoption`.
        The individual ids are `paidnochange`, `markpaid`, and `marknotpaid`.
        The javascript and python code both use these values.

Lines 37, 43
        When using bootsnipp, 
        pay close attention to the name and id for these two input elements
        for the Pickup Options radio buttons.
        The name of both radio buttons is `pickedup`.
        The individual ids are `pickedup` and `notpickedup`.
        The javascript and python code both use these values.

Lines 54 and 55
        When using bootsnipp,
        make sure the id for these two buttons 
        are correct and correspond to the javascript.
        The ids are `clear` and `action`.
        The javascript uses these.

Line 63
        This line must be added to the code you get from bootsnipp.
        It is a hidden form element to contain the name of the python script.
        You see `{{pyscript}}` which will be replaced with
        the name of the Python script file.
        `model.Data.pyscript` is set internally to the name of the Python Script file.
        Any time you use a form like this in a project that posts its results, 
        this hidden element is required.
        
        .. note::
                The double curly braces are known as handlebar notations 
                (think of bicycle handle bars). 

                Handlebars is the library we use to replace values for HTML content. 

                Anything in the `model.Data` object 
                is available for use with the Handlebars.
                In addition to any values you assign to this object, 
                all form variables are posted to this object as well.

Line 64
        The name of the input textbox should be `wandtarget` 
        to match the javascript and the python code that uses this value.

Line 66
        The value of the input textbox for the wandtarget is set from the post event 
        with the `{{wandtarget}}` handlebar directive.
        `model.Data.wandtarget` is set when the form is posted by the user.

Lines 71-74
        These contain the div which will be used to display any messages 
        you return using the `print` statement. 
        The div must have an id of `output` for this to work.

        Section to be added:

        .. code-block:: html
          
            <!-- Notice Area -->
            <div class="form-group">
              <div id="output" class="col-md-4 col-md-offset-4"></div>
            </div>

