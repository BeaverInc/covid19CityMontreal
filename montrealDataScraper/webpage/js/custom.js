var borough = ["Ahuntsic–Cartierville", "Anjou", "Baie-D'Urfé", "Beaconsfield", "Côte-des-Neiges–Notre-Dame-de-Grâce", "Côte-Saint-Luc", "Dollard-des-Ormeaux", "Dorval", "Hampstead", "Kirkland", "Lachine", "LaSalle", "L'Île-Bizard–Sainte-Geneviève", "Mercier–Hochelaga-Maisonneuve", "Montréal-Est", "Montréal-Nord", "Montréal-Ouest", "Mont-Royal", "Outremont", "Pierrefonds–Roxboro", "Plateau-Mont-Royal", "Pointe-Claire", "Rivière-des-Prairies–Pointe-aux-Trembles", "Rosemont–La Petite Patrie", "Sainte-Anne-de-Bellevue", "Saint-Laurent", "Saint-Léonard", "Senneville", "Sud-Ouest", "Verdun", "Ville-Marie", "Villeray–Saint-Michel–Parc-Extension", "Westmount"]


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
    $("#area_c").append('<img id="'+name+'_case'+'" src=montrealDataScraper/webpage/graph/cases/'+name+'_c.png>');
    $("#area_d").append('<img id="'+name+'_double'+'" src=montrealDataScraper/webpage/graph/double_time/'+name+'_d.png>');
    $("#map").append('<img id="'+name+'" src=montrealDataScraper/webpage/graph/map/'+name+'.PNG class ="mx-auto d-block">');
    alert( case_address );
});
