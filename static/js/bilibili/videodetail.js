$(function() {
    var video_recent_week = function(){
      var av_id = $('input[id="av_id"]').val();
      var _video_recent_week = $.get('/api/bilibili/video/'+ av_id +'/recent_week/',
        function(data){
          _show_chart(data);
        });
    };
    var _show_chart = function(data){
      var arr = new Array();
      for(var i=0;i<data.length;i++){
        // 拼装数据
        arr.push({
          period: data[i].createtime,
          view: data[i].view,
        });
        console.log(arr);
      };
      var charts_dict = {
          element: 'morris-area-chart',
          data: arr,
          xkey: 'period',
          ykeys: ['view'],
          labels: ['view'],
          pointSize: 2,
          hideHover: 'auto',
          resize: true
      }
      console.log(charts_dict);
      Morris.Area(charts_dict);
    };
    video_recent_week();


});
