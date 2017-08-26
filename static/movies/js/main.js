
$(function() {
    var page_cur = 1;
    var has_next_page = true;

    var fetch_movies_list = function(page){
    $.ajax({
        url: '/api/movies/?page=' + page,
        type: 'GET',
        data: '',
        success: function(data){
            refresh_html(data.results);
            if(data.next==null || data.next=='null'){
                has_next_page = false;
            }
        },
        error: function(data){
            console.log('error')
        },
        });
    };

    var refresh_html = function(items){
        $('#movies-list').empty();
        for(var i=0;i < items.length; i++){
            html = '<li class="yk-col4 mr1">' +
                '<div class="yk-pack pack-film">'+
                    '<div class="p-thumb"><a href="/movies/play/?v='+ items[i].url +'"'+
                                            'title="'+ items[i].title +'" target="_blank" data-spm-anchor-id="a2h1n.8251845.0.0"></a><i'+
                            'class="bg"></i><img class="quic" _src=""'+
                                                'src="'+ items[i].bg_img_url +'" alt="'+ items[i].title +'"></div>'+
                    '<ul class="p-info pos-bottom">'+
                        '<li class="status hover-hide"><span class="p-time "><i class="ibg"></i><span>正片</span></span></li>'+
                    '</ul>'+
                    '<ul class="info-list">'+
                        '<li class="title"><a href="//v.youku.com/v_show/id_XMTUzNzM1MjUwMA==.html" title="'+ items[i].title +'" target="_blank">'+ items[i].title +'</a>'+
                        '</li>'+
                        '<li class="actor"><em>主演：</em><a href="" target="_blank"'+
                                                         'title="'+ items[i].lead_actor +'">'+ items[i].lead_actor +'</a>'+
                         '</li>'+
                        '<li>2.4万次播放</li>'+
                    '</ul>' +
                '</div>' +
            '</li>'
            $('#movies-list').append(html)
        }

    };

    var fetch_page = function(){
        fetch_movies_list(page_cur);
    };

    $('.next').on('click', function(){
        if(has_next_page){
            page_cur++;
            fetch_page();
        }else{
            alert('没有下一页了')
        };

    });

    $('.previous').on('click', function(){
        if(page_cur > 1){
            page_cur--;
            fetch_page()
        }else{
            alert('已经是第一页')
        };

    });

    fetch_page()

})
