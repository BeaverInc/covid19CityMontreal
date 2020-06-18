var placeholder = "placeholder_text"



$(function(){

    var select = document.getElementById("borough_select");

    for(var i = 0; i < borough.length; i++) {
        var opt = borough[i];
        var ele = document.createElement('option');
        ele.value = opt
        ele.classList = "selected";
        var borough_name_string = opt;
        ele.innerText = "" + opt;
        document.querySelector(".custom-select").appendChild(ele);
    }

});


$('select').on('change', function() {
    var name = this.value;

    var name_url = name;
    if (/\s/.test(name)){
        name_url = name_url.replace(/\s/g, "%20");
    }

    var name_in_js = name;
    name_in_js = name_in_js.replace(/\s/g, "_").replace(/'/g, "_").replace(/-/g, "_").replace(/–/g, "_");
    var report_data = window[name_in_js];

    $("#area_c").empty();
    $("#area_d").empty();
    $("#area_n").empty();
    $("#map").empty();
    $("#cumulative_case").empty();
    $("#new_case").empty();
    if(name!="Montreal"){
        $("#area_c").append('<img id="'+name+'_case'+'"src="graph/cases/'+name_url+'_c.png" class ="mx-auto d-block img-fluid"> ');
        $("#area_d").append('<img id="'+name+'_double'+'"src="graph/double_time/'+name_url+'_d.png" class ="mx-auto d-block img-fluid">');
        $("#area_n").append('<img id="'+name+'_new'+'"src="graph/new/'+name_url+'_n.png" class ="mx-auto d-block img-fluid">');
        $("#cumulative_case").append("On "+report_data.cumulativeCasesDate+" , cumulative cases in "+name+" : "+"<b>"+report_data.cumulativeCases+"</b>");
        $("#new_case").append("On "+report_data.newCasesDate+" , new cases in "+name+" : "+"<b>"+report_data.newCases+"</b>" );

    }
    $("#map").append('<img id="'+name+'"src="graph/map/'+name_url+'.png" class ="mx-auto d-block img-fluid">');

});

