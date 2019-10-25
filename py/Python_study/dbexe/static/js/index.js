$(document).ready(function() {
    if(/index_instance\/(\w+)/.test(location.href)) {
        let val = RegExp.$1;
        $("#instance_name").val(val);
    }
   $("#instance_name").change(function () {
       let value = $(this).val();
       let href = location.href;
       if (href.indexOf("index_instance") > -1) {
           location.href = location.href.replace(/index_instance\/\w+/, 'index_instance/'+value);
       } else {
            location.href = location.href + "index_instance/" + value;
       }
   })
    $("#selectAll").change(function () {
        let check = $(this).prop("checked");
            $("#db_name").find("input").each(function () {
                $(this).prop("checked", check)
            })
    })
    $("#deSelect").change(function () {
        $("#db_name").find("input").each(function () {
            $(this).prop("checked", !$(this).prop("checked"))
        })
    })
});