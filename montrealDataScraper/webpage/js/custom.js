
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
    $("#area_c").empty()
    $("#area_d").empty()
    $("#map").empty()
    $("#area_c").append('<img id="'+name+'_case'+'" src=montrealDataScraper/webpage/graph/cases/'+name+'_c.png class ="mx-auto d-block img-fluid"> ');
    $("#area_d").append('<img id="'+name+'_double'+'" src=montrealDataScraper/webpage/graph/double_time/'+name+'_d.png class ="mx-auto d-block img-fluid">');
    $("#map").append('<img id="'+name+'" src=montrealDataScraper/webpage/graph/map/'+name+'.png class ="mx-auto d-block img-fluid">');
});
