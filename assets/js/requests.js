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
        html += '<li>' + v.fields.info + '</li>';
    });

    return html + '</ul>';
}
function update_requests_info() {
    $.post(document.location.href, {ids: read_ids()}, function (resp) {
        last_resp = resp;
        update_title_val(resp['total']);
        $("#requests").html(render_requests_list());
    }, 'json');
}
$(document).ready(function () {
    setInterval(update_requests_info, 3000);
    update_requests_info();
});