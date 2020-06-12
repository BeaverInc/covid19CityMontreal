
$(function(){
    var select = document.getElementById("c_area");
    for(var i = 0; i < borough.length; i++) {

        var name = borough[i];
        var name_url = name;
        if (/\s/.test(name)){
            name_url = name_url.replace(/\s/g, "%20");
        }
        $("#c_area").append( '<div class="col-sm-12 col-md-12 col-lg-12 col-xl-6"><img src="graph/cases/'+name_url+'_c.png" class="mx-auto d-block img-fluid""></div>');
    }
});



