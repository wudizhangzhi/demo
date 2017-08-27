
$(function() {
    var fetch_movies_list = function(page){
    $.ajax({
        url: '/api/movies/?page=' + page,
        type: 'GET',
        data: '',
        success: function(data){
            refresh_html(data);
        },
        error: function(data){
            console.log('error')
        },
        });
    };

    var refresh_html = function(data){
        $('#movies-list').empty();
        for(item in data){
            html = '<li class="yk-col4 mr1">' +
                '<div class="yk-pack pack-film">'+
                    '<div class="p-thumb"><a href="'+ item.url +''"'+
                                            'title="'+ item.title +'" target="_blank" data-spm-anchor-id="a2h1n.8251845.0.0"></a><i'+
                            'class="bg"></i><img class="quic" _src=""'+
                                                'src="'+ item.bg_img_url +'" alt="'+ item.title +'"></div>'+
                    '<ul class="p-info pos-bottom">'+
                        '<li class="status hover-hide"><span class="p-time "><i class="ibg"></i><span>正片</span></span></li>'+
                    '</ul>'+
                    '<ul class="info-list">'+
                        '<li class="title"><a href="//v.youku.com/v_show/id_XMTUzNzM1MjUwMA==.html" title="'+ item.title +'" target="_blank">'+ item.title +'</a>'+
                        '</li>'+
                        '<li class="actor"><em>主演：</em><a href="" target="_blank"'+
                                                         'title="'+ item.lead_actor +'">'+ item.lead_actor +'</a>'+
                         '</li>'+
                        '<li>2.4万次播放</li>'+
                    '</ul>' +
                '</div>' +
            '</li>'
            $('#movies-list').append(html)
        }

    };



    fetch_movies_list(1);

})
