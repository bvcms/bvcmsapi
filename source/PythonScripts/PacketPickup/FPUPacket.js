$(function () {
    $("#wandtarget").keypress(function(ev) {
        if (ev.which !== 13)
            return true;
        $.action();
        return false;
    });
    $("#action").click(function(ev) {
        ev.preventDefault();
        $.action();
        return false;
    });
    $.action = function() {
        var v = $("#wandtarget").val();
        if ((v.split("-").length - 1) > 1) {
            $("#wandtarget").val('');
            $("#output").html('');
            return;
        }
        var q = $("#wandform").serialize();
        $.post("/PyScriptForm/", q, function (ret) {
            $("#output").html(ret);
            $("#wandtarget").focus();
        });
    };
    $("#clear").click(function(ev) {
        ev.preventDefault();
        if($("#paidnochange").is(':checked') && $("#pickedup").is(':checked'))
            $("#wandtarget").val('').focus();
        else {
            $('#paidnochange').prop('checked', true);
            $('#pickedup').prop('checked', true);
        }
        $("#output").html("");
    });
    $("#wandtarget").focus();
});

