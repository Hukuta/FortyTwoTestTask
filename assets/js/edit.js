$(document).ready(function () {
    if ($("#id_first_name").length) {
        var main_form = $("#main_form");
        var input = main_form.find('input'),
            textarea = main_form.find('textarea');

        $(document).ajaxError(function () {
            input.each(function () {
                $(this).removeAttr('disabled')
            });
            textarea.each(function () {
                $(this).removeAttr('disabled')
            });
            $("#ajax_answer").text('Server Error!');
            setTimeout(function () {
                $("#ajax_answer").text('');
            }, 2000);
        });
        var serialized;
        var options = {
            target: '#ajax_answer',   // target element(s) to be updated with server response
            beforeSubmit: function () {// pre-submit callback
                serialized = main_form.serialize();
                input.each(function () {
                    $(this).attr('disabled', 'disabled')
                });
                $('.errors').remove();
            },
            success: function (data, statusText, xhr, $form) {
                if (data === 'OK') {
                    $("#ajax_answer").text('Saved!');
                    setTimeout(function () {
                        $("#ajax_answer").text('');
                    }, 2000);
                } else {
                    $.each(data, function (field, errors) {
                        var err_div = $('#error_' + field);
                        if(!err_div.length){
                            $('#id_' + field).before('<div class="errors" id="error_'+field+'"></div>');
                            err_div = $('#error_' + field);
                        }
                        $.each(errors, function (er, er_mess) {
                            err_div.append('<p>' + er_mess + '</p>')
                        });
                    });
                }
                input.each(function () {
                    $(this).removeAttr('disabled')
                });
                textarea.each(function () {
                    $(this).removeAttr('disabled')
                });
            },  // post-submit callback

            type:      'post',        // 'get' or 'post', override for form's 'method' attribute
            dataType:  'json',        // 'xml', 'script', or 'json' (expected server response type)
            clearForm: false,        // clear all form fields after successful submit
            resetForm: false        // reset the form after successful submit
        };

        main_form.submit(function (e) {
            e.preventDefault();
            $(this).ajaxSubmit(options);
            return false; // never submit directly
        });
    }// else - auth form

});