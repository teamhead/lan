function query() {
    var data = $("form").serializeArray();
    $.ajax({
        type: "POST",
        contentType: "application/json;charset=UTF-8",
        url: "http://sqlmanager.e6gpshk.com/query_data/",
        data: JSON.stringify(data),
        success: function(result) {
            showdata(JSON.parse(result));
        },
        error: function(e) {
            console.log(e.status);
            console.log(e.responseText);
            $("#content").html(e.status);
            $("#tipModal").modal("show");
        },
    });
}

function showdata(result) {
    $("#page").Page({
        totalPages: Math.ceil(result.length / 10), //total Pages
        liNums: 10, //the li numbers(advice use odd)
        activeClass: 'activeP', //active class style
        firstPage: '首页', //first button name
        lastPage: '末页', //last button name
        prv: '?', //prev button name
        next: '?', //next button name
        hasFirstPage: true, //whether has first button
        hasLastPage: true, //whether has last button
        hasPrv: false, //whether has prev button
        hasNext: false, //whether has next button
        callBack: function(page) {
            renderData(result.slice((page - 1) * 10, Math.min(page * 10, result.length)));
        }
    });
    renderData(result.slice(0, Math.min(10, result.length)));
}

function renderData(data) {
    $('#table-content').html('');
    var html = data.reduce((p, c) => {
        c.key = c.key.replace(/['"]/g, '');
        c.db_name = c.db_name.replace(/['"]/g, '');
        c.sql_message = c.sql_message.replace(/['"]/g, '').replace(/\s+/g, '&nbsp;');
        c.type = c.type.replace(/['"]/g, '');
        c.description = c.description.replace(/['"]/g, '').replace(/\s+/g, '&nbsp;');

        p += `<tr class="td-style">
            <td title=${c.key}>${c.key}</td>
            <td title=${c.db_name}>${c.db_name}</td>
            <td title=${c.sql_message}>${c.sql_message}</td>
            <td title=${c.type}>${c.type}</td>
            <td title=${c.mon_interval}>${c.mon_interval}</td>
            <td title=${c.description}>${c.description}</td>
        </tr>`;
        return p;
    }, '');
    $('#table-content').html(html);
};
$(function() {
    $('#addModal').on('hide.bs.modal', function() {
        $(this).find('input').val('');
        $(this).find('select').val('');
    })
    $("#add").click(function(e) {
        var ev = e || window.event;
        ev.preventDefault();
        $('#addModal').modal('show');
    })
    $("#key").get(0).oninput = function() {
        var v = $(this).val();
        $('#db_name').prop('readonly', !!v);
        $("#queryTime").prop('disabled', !!v);
    }
})



function inst() {
    var data = $(".form").serializeArray();
    console.log(data)
    $.ajax({
        type: "POST",
        contentType: "application/json;charset=UTF-8",
        url: "http://sqlmanager.e6gpshk.com/ins_zabbix/",
        data: JSON.stringify(data),
        success: function(result) {
            showdata(result)
        },
        error: function(e) {
            // showdata(result);
            console.log(e.status);
            console.log(e.responseText);
            $("#content").html(e.status);
            $("#tipModal").modal("show");
        },
    });
}
