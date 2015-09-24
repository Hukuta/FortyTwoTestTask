var title = $("title");
var last_resp = {total: 0, requests: []};

function update_title_val(total) {
    title.text(title.text().replace(/^\(\d+\)/, '(' + total + ')'));
}
function read_ids() {
    var ids = [];
    $.each(last_resp['requests'], function (i, v) {
        ids.push(v.pk);
    });
    return ids;
}
function render_requests_list() {
    var html = '<ul>';
    $.each(last_resp['requests'], function (i, v) {
        html += '<li><label onclick="$(this).find(\'input\').addClass(\'priority-box\')">'
            + 'Priority <input type="checkbox" data-id="'
            + v.pk + '" '
            + (v.fields.priority=='1' ? 'checked="checked"' : '') + '></label> '
            + v.fields.info + '</li>';
    });

    return html + '</ul>';
}
function get_ids_with_priority(checked) {
    var return_ids = [];
    $(".priority-box").each(function () {
        if ($(this).prop('checked') == checked)
            return_ids.push($(this).attr('data-id'))
    });
    return return_ids;
}
function update_requests_info() {
    $.post(document.location.href, {
        ids: read_ids(),
        priority0: get_ids_with_priority(false),
        priority1: get_ids_with_priority(true)
    }, function (resp) {
        last_resp = resp;
        update_title_val(resp['total']);
        $("#requests").html(render_requests_list());
    }, 'json');
}
$(document).ready(function () {
    setInterval(update_requests_info, 3000);
    update_requests_info();
});