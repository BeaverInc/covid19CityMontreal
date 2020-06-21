var english = {
    title:"Montreal, Covid 19 data in each borough",
    home:"Home",case:"Cumulative Cases",
    double:"Doubling Time",
    new:"New Case Everyday",
    date_disclaimer:" All data is collected from:",
    before_text_update_time:"Last updated on\xa0",
    latest_data:"Latest Data:",
    select_borough:"Select a borough in Montreal...",
    on:"On\xa0"
};

var chinese = {
    title:"蒙特利尔市，各行政区新冠病毒数据",
    home:"主页",case:"累计确诊人数",
    double:"倍增时间",new:"每日新增确诊数",
    date_disclaimer:" 所有数据均来自于：",
    before_text_update_time:"最后更新时间：",
    latest_data:"最新数据:",
    select_borough:"从蒙特利尔市内选择一个行政区...",
    on:""
};


$(document).ready(function() {
    $("#translation :input").change(translation);
});

function translation()  {
    var script_file = window[this.value];

    $('title').text(script_file.title);
    $("#graph_title_case").text(script_file.case);
    $("#graph_title_double").text(script_file.double);
    $("#graph_title_new").text(script_file.new);
    $("#home-radio").get(0).nextSibling.textContent=script_file.home;
    $("#case-radio").get(0).nextSibling.textContent=script_file.case;
    $("#double-radio").get(0).nextSibling.textContent=script_file.double;
    $("#new-radio").get(0).nextSibling.textContent=script_file.new;
    $("#date_disclaimer").text(script_file.date_disclaimer);
    $("#before_text_update_time").text(script_file.before_text_update_time);
    $("#latest_data").text(script_file.latest_data);
    $("#select_borough").text(script_file.select_borough);

};
