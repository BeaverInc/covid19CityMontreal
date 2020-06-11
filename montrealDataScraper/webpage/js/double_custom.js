
$(function(){
    var select = document.getElementById("d_area");
    for(var i = 0; i < borough.length; i++) {
        var name = borough[i];
        $("#d_area").append( '<div class="col-sm-12 col-md-12 col-lg-12 col-xl-6"><img src="graph/double_time/'+name+'_d.png" class="mx-auto d-block img-fluid""></div>');
    }
});



