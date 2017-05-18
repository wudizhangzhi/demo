$(function() {
    var uper_top = function(){
      var _uper_top_10 = $.get('/api/bilibili/data/uper_top/',
        function(data){
          _show_chart(data);
          console.log('start uper top')
        });
    };
    var _show_chart = function(data){
      var arr = new Array();
      for(var i=0;i<data.length;i++){
        // 拼装数据
        arr.push({
          name: data[i].name,
          fans: data[i].fans,
        });
      };
      var charts_dict = {
          element: 'morris-bar-chart',
          data: arr,
          xkey: 'name',
          ykeys: ['fans'],
          labels: ['粉丝数量'],
          hideHover: 'auto',
          resize: true
      }
      Morris.Bar(charts_dict);
    };
    uper_top();

    var video_top = function(){
      var _uper_top_10 = $.get('/api/bilibili/data/video_top/',
        function(data){
          _show_chart_uper(data);
          console.log('start video top');
        });
    };
    var _show_chart_uper = function(data){
      var arr = new Array();
      for(var i=0;i<data.length;i++){
        // 拼装数据
        arr.push({
          title: data[i].title,
          view: data[i].view,
        });
      };
      var video_dict = {
          element: 'topvideo-bar-chart',
          data: arr,
          xkey: 'title',
          ykeys: ['view'],
          labels: ['观看数量'],
          hideHover: 'auto',
          resize: true
      }
      Morris.Bar(video_dict);
    };
    video_top();
});
