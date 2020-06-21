$(function(){
    page_initialization();
    $(document).ready(function() {
        $("#radio_btn :input").change(hide_n_show);
    });
    borough_selector();
    time_updater();

});

function page_initialization()  {
    for(var i = 0; i < borough.length; i++) {
        var name = borough[i];
        var name_url = name;
        if (/\s/.test(name)){
            name_url = name_url.replace(/\s/g, "%20");
        }
        $("#c_area").append( '<div class="col-sm-12 col-md-12 col-lg-12 col-xl-6"><img src="graph/cases/'+name_url+'_c.png" class="mx-auto d-block img-fluid""></div>');
        $("#n_area").append( '<div class="col-sm-12 col-md-12 col-lg-12 col-xl-6"><img src="graph/new/'+name_url+'_n.png" class="mx-auto d-block img-fluid""></div>');
        $("#d_area").append( '<div class="col-sm-12 col-md-12 col-lg-12 col-xl-6"><img src="graph/double_time/'+name_url+'_d.png" class="mx-auto d-block img-fluid""></div>');
    }

    $('.card').hide();
    $("#home").show();


};



function hide_n_show()  {
    $('.card').hide();
    $("#"+this.value).show();

};

function time_updater(){
    var select = document.getElementById("update_time");
    var time = record_time;
    $("#update_time").text(time);
};

function borough_selector(){
    // adding selector on page
    for(var i = 0; i < borough.length; i++) {
        var opt = borough[i];
        var ele = document.createElement('option');
        ele.value = opt
        ele.classList = "selected";
        ele.innerText = "" + opt;
        document.querySelector(".custom-select").appendChild(ele);
    }


    //apply selector
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
};