var chart = echarts.init(document.getElementById('ncov-map'), 'white', {renderer: 'canvas'});
// var p_chart = echarts.init(document.getElementById('pmap-chart'), 'white', {renderer: 'canvas'});
var loader = document.getElementById('loading');
var iframe = document.getElementById('pmap-chart');
iframe.onreadystatechange=function() {
		//此事件在内容没有被载入时候也会被触发，所以我们要判断状态
		//有时候会比较怪异 readyState状态会跳过 complete 所以我们loaded状态也要判断
        loader.css.dispaly = "";
		if (iframe.readyState === "complete" || iframe.readyState === "loaded"){
		    loader.css.dispaly = "none"
        }
	};


$(
    function () {
        updateOverall();
        updateNews();
        fetchData(chart);
        setInterval(updateNews, 60 * 1000);
        setInterval(updateOverall, 60 * 1000);
        setInterval(fetchData, 30 * 60 * 1000);
    }
);
chart.on('click', function (param) {
    if (isNaN(param.name.charAt(0))){
         iframe.src = getHost()+'/pmap/'+param.name;
         var myModal = $("#chart-modal");
         myModal.modal("show");
    }
    // window.open(getHost()+'/pmap/'+param.name)




});
function getHost() {
    return document.location.protocol + "//" +window.location.host;
}

function updateOverall(){
    $.ajax({
        type: "GET",
        url: getHost() + "/overall",
        dataType: 'json',
        success: function (result) {

            var t = new Date()

            overall_html = '<li class="text-muted"><i class="fa fa-bug pr-2"></i>病毒：' + result['results'][0]['virus'] + '</li><li class="text-muted"><i class="fa fa-bolt pr-2"></i>源头：' + result['results'][0]['infectSource'] + '</li><li class="text-muted"><i class="fa fa-hospital-o pr-2"></i>  疑似病例：' + result['results'][0]['suspectedCount'] + '</li><li class="text-muted"><i class="fa fa-heartbeat pr-2"></i>确诊病例：' + result['results'][0]['confirmedCount'] + '</li><li class="text-muted"><i class="fa fa-hospital-o pr-2"></i>死亡病例：' + result['results'][0]['deadCount'] + '</li><li class="text-muted"><i class="fa fa-clock-o pr-2"></i>更新时间：' + result['time'] + '</li>'
            $('#overall').html(overall_html)
        }
    });
}

function updateNews(){
    $.ajax({
        type: "GET",
        url: getHost() + "/news",
        dataType: 'json',
        success: function (result) {
            news_html = ""
            for(var i = 0, len = result.length; i < len; i++){
                news_html += "<li><div class='base-timeline-info'><a href=" + result[i]['sourceUrl'] + ">" + result[i]['title'] + "</a></div><small class='text-muted'>" + result[i]['infoSource'] + '</small></li>'
            }
            $('#newslist').html(news_html)
        }
    });
}

function fetchData() {
    $.ajax({
        type: "GET",
        url: getHost() + "/map",
        dataType: 'json',
        success: function (result) {
            chart.setOption(result);
        }
    });
}
