$(document).ready(function() {
    // 添加实例信息
    function add_instance(e) {
        var ev1 = e || window.event;
        ev1.preventDefault();
        var data = $("form").serializeArray();
        console.log(data)
        $.ajax({
            //请求方式
            type: "POST",
            //请求的媒体类型
            contentType: "application/json;charset=UTF-8",
            //请求地址
            url: "http://sqlmanager.e6gpshk.com/ins_instance/",
            //数据，json字符串
            data: JSON.stringify(data),
            //请求成功
            success: function(result) {

                data = JSON.parse(result);
                //alert(data);
                //db_name_indo(data);
                $("#content").html(data.status);
                $("#tipModal").modal("show");
            },
            //请求失败，包含具体的错误信息
            error: function(e) {
                console.log(e.status);
                console.log(e.responseText);
                $("#content").html(e.status);
                $("#tipModal").modal("show");
            },
            // complete: function(res) {
            //     $("#content").html(res.status);
            //     $("#tipModal").modal("show");
            // }
        });

    };

    function update_ins() {

        var data = $("form").serializeArray();
        $.ajax({
            //请求方式
            type: "POST",
            //请求的媒体类型
            contentType: "application/json;charset=UTF-8",
            //请求地址
            url: "http://sqlmanager.e6gpshk.com/ins_db/",
            //数据，json字符串
            data: JSON.stringify(data),
            //请求成功
            success: function(result) {
                data = JSON.parse(result);
                console.log(data);
                // window.location.reload();
                $("form").find("[name]").val("");
                $("#content").html(data.status);
                $("#tipModal").modal("show");
            },
            //请求失败，包含具体的错误信息
            error: function(e) {
                console.log(e.status);
                console.log(e.responseText);
                $("form").find("[name]").val("");
                $("#content").html(e.status);
                $("#tipModal").modal("show");
            }
        });
    };

    function add_db(e) {

        var data = $("form").serializeArray();
        $.ajax({
            //请求方式
            type: "POST",
            //请求的媒体类型
            contentType: "application/json;charset=UTF-8",
            //请求地址
            url: "http://sqlmanager.e6gpshk.com/ins_db/",
            //数据，json字符串
            data: JSON.stringify(data),
            //请求成功
            success: function(result) {
                data = JSON.parse(result)
                alert(data[status])
            },
            //请求失败，包含具体的错误信息
            error: function(e) {
                console.log(e.status);
                console.log(e.responseText);
            }
        });

    };

    function validateCall($element, errorCondition) {
        let flag = false;
        let val = $element.val();
        let parent = $element.parents(".form-group");
        if (!val) {
            if (!parent.hasClass("has-error")) {
                parent.addClass("has-error");
            }
            parent.find(".glyphicon").show();
            parent.find(".error-text").show();
        } else {
            if (errorCondition(val)) {
                if (!parent.hasClass("has-error")) {
                    parent.addClass("has-error");
                }
                parent.find(".glyphicon").show();
                parent.find(".error-text").show();
            } else {
                if (parent.hasClass("has-error")) {
                    parent.removeClass("has-error");
                }
                parent.find(".glyphicon").hide();
                parent.find(".error-text").hide();
                flag = true;
            }
        }
        return flag;
    }

    function validate($element, errorCondition) {
        $element.get(0).oninput = function() {
            let val = $(this).val();
            let parent = $(this).parents(".form-group");
            if (!val) {
                if (parent.hasClass("has-error")) {
                    parent.removeClass("has-error");
                }
                parent.find(".glyphicon").hide();
                parent.find(".error-text").hide();
            } else {
                if (errorCondition(val)) {
                    if (!parent.hasClass("has-error")) {
                        parent.addClass("has-error");
                    }
                    parent.find(".glyphicon").show();
                    parent.find(".error-text").show();
                } else {
                    if (parent.hasClass("has-error")) {
                        parent.removeClass("has-error");
                    }
                    parent.find(".glyphicon").hide();
                    parent.find(".error-text").hide();
                    // flag = true;
                }
            }
        }
    };
    validate($("#easname"), function(val) {
        return !val;
    });
    validate($("#ipaddr"), function(val) {
        return !/((25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))\.){3}(25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))/.test(val);
    });
    validate($("#db_port"), function(val) {
        return !/\d+/.test(val) || (+val < 0 || +val > 65535)
    });
    validate($("#username"), function(val) {
        return val.length < 8 || val.length > 16;
    });
    validate($("#passwd"), function(val) {
        return !val;
    });
    $("#add_ins").click(function(e) {
        var ev2 = e || window.event;
        ev2.preventDefault();
        var res = validateCall($("#easname"), function(val) {
            return !val;
        }) & validateCall($("#ipaddr"), function(val) {
            return !/((25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))\.){3}(25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))/.test(val);
        }) & validateCall($("#db_port"), function(val) {
            return !/\d+/.test(val) || (+val < 0 || +val > 65535)
        }) & validateCall($("#passwd"), function(val) {
            return !val;
        })
        if (res) {
            add_instance(e);
        }

    })
    $("#update_ins").click(function(e) {
        var ev2 = e || window.event;
        ev2.preventDefault();
        var res = validateCall($("#easname"), function(val) {
            return !val;
        }) & validateCall($("#ipaddr"), function(val) {
            return !/((25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))\.){3}(25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))/.test(val);
        }) & validateCall($("#db_port"), function(val) {
            return !/\d+/.test(val) || (+val < 0 || +val > 65535)
        }) & validateCall($("#passwd"), function(val) {
            return !val;
        })
        if (res) {
            update_ins();
        }

    })
})
