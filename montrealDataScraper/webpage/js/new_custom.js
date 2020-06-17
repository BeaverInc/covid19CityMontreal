
$(function(){
    var select = document.getElementById("n_area");
    for(var i = 0; i < borough.length; i++) {
        var name = borough[i];
        var name_url = name;
        if (/\s/.test(name)){
            name_url = name_url.replace(/\s/g, "%20");
        }
        $("#n_area").append( '<div class="col-sm-12 col-md-12 col-lg-12 col-xl-6"><img src="graph/new/'+name_url+'_n.png" class="mx-auto d-block img-fluid""></div>');
    }
});



