$(document).ready((function() {
    // 获取实例信息
    $.get("http://sqlmanager.e6gpshk.com/select_instance/", function(data) {
        data = JSON.parse(data);
        var html = Object.keys(data).reduce((p, key) => {
            p += `<option style='display: none'></option><option value=${data[key]}>${data[key]}</option>`;
            return p
        }, "");
        $("#instance_name").html(html);
        $("#instance_name_store").html(html);
    });
    // 通过ajax的post请求获取数据库信息
    $('#instance_name').change(function() {
        // 定义实例信息
        var instance_name = $(this).val();
        console.log(instance_name);
        var url = "http://sqlmanager.e6gpshk.com/select_db/";
        create_post_ajax(instance_name, url)
    });
    // 全选
    $("#selectAll").change(function() {
        let check = $(this).prop("checked");
        $("#db_name").find("input").each(function() {
            $(this).prop("checked", check)
        })
    });
    // 调用反选
    $("#deSelect").change(function() {
        checkNotAll();
    });
    // 判断工作模式，加载相应的输入框
    $("#OperType").change(function() {
        var OperType = $(this).val();
        loadInput(OperType);
    });
}));

//被调用的ajax post请求
function create_post_ajax(instance_name, url) {
    //请求参数
    var name = instance_name;
    //
    $.ajax({
        //请求方式
        type: "POST",
        //请求的媒体类型
        contentType: "application/json;charset=UTF-8",
        //请求地址
        url: url,
        //数据，json字符串
        data: JSON.stringify(name),
        //请求成功
        success: function(result) {
            db_name_info(result);
        },
        //请求失败，包含具体的错误信息
        error: function(e) {
            console.log(e.status);
            console.log(e.responseText);
        }
    });
}
// 循环遍历获取到的数据并加载到<select>
function db_name_info(result) {
    data = JSON.parse(result);
    var html = "";
    data.forEach(e => {
        html += `<div><input type="checkbox" value='${e}' name="db_name" />${e}</div>`;
    });
    $("#db_show_name").html(html);
}

// 被调用反选
function checkNotAll() {
    $("#db_name").find("input").each(function() {
        $(this).prop("checked", !$(this).prop("checked"))
    })
}

// 点击提交按钮执行的操作
function back_submit() {
    var data = $("form").serializeArray();
    console.log(data);
    $.ajax({
        //请求方式
        type: "POST",
        //请求的媒体类型
        contentType: "application/json;charset=UTF-8",
        //请求地址
        url: "http://sqlmanager.e6gpshk.com/backup/",
        //数据，json字符串
        data: JSON.stringify(data),
        //请求成功
        success: function(result) {
            alert('数据已提交');
            window.location.reload();
        },
        //请求失败，包含具体的错误信息
        error: function(e) {
            console.log(e.status);
            console.log(e.responseText);
        }
    });
}
// 根据操作选项控制标签的隐藏
function loadInput(OperType) {
    if (OperType == "备份") {
        $(".Restore_createUser").hide();
        $(".BackUp").show();
        $(".Restore").hide();
        $(".userWork").hide();
        $('.ShowSql').hide();
    };
    if (OperType == "还原") {
        $(".Restore_createUser").show();
        $(".BackUp").hide();
        $(".Restore").show();
        $(".userWork").hide();
        $('.ShowSql').show();
    };
    if (OperType == "创建账户") {
        $(".Restore_createUser").show();
        $(".BackUp").hide();
        $(".Restore").hide();
        $(".userWork").show();
        $('.ShowSql').show();
    };
}
// 点击生成sql语句按钮触发的事件
function GetSql() {
    var data = $("form").serializeArray();
    $.ajax({
        //请求方式
        type: "POST",
        //请求的媒体类型
        contentType: "application/json;charset=UTF-8",
        //请求地址
        url: 'http://127.0.0.1/exe_sql/',
        //数据，json字符串
        data: JSON.stringify(data),
        //请求成功
        success: function(result) {
            data = JSON.parse(result)
            $("#show-sql").val(data);
        },
        //请求失败，包含具体的错误信息
        error: function(e) {
            console.log(e.status);
            console.log(e.responseText);
        }
    });
}
