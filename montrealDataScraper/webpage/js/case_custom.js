
$(function(){
    var select = document.getElementById("c_area");
    for(var i = 0; i < borough.length; i++) {
        var name = borough[i];
        $("#c_area").append( '<div class="col-sm-12 col-md-12 col-lg-12 col-xl-6"><img src="graph/cases/'+name+'_c.png" class="mx-auto d-block img-fluid""></div>');
    }
});



