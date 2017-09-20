$(function() {
    var video_recent_week = function(){
      var uper_id = $('input[id="uper_id"]').val();
      var _video_recent_week = $.get('/api/bilibili/uper/'+ uper_id +'/recent_week/',
        function(data){
          _show_chart(data);
        });
    };
    'videonum', 'gz', 'fans', 'play'
    var _show_chart = function(data){
      var arr = new Array();
      for(var i=0;i<data.length;i++){
        // 拼装数据
        arr.push({
          period: data[i].createtime,
          videonum: data[i].videonum,
          gz: data[i].gz,
          fans: data[i].fans,
          play: data[i].play,
        });
      };
      var charts_dict = {
          element: 'morris-area-chart',
          data: arr,
          xkey: 'period',
          ykeys: ['videonum', 'gz', 'fans', 'play'],
          labels: ['视频数量', '分享数量', '粉丝数量', '播放数量'],
          pointSize: 2,
          hideHover: 'auto',
          resize: true
      }
      Morris.Area(charts_dict);
    };
    video_recent_week();


});
