
$(function() {
    var page_cur = 1;
    var has_next_page = true;


    function GetQueryString(name)
    {
         var reg = new RegExp("(^|&)"+ name +"=([^&]*)(&|$)");
         var r = window.location.search.substr(1).match(reg);
         if(r!=null)return  unescape(r[2]); return null;
    }

    function search(v){
        _url = '/api/movies/movies/?'
        _search = search?'&search=' + search:'';
        _url = _url + _search;
        $.ajax({
            url: _url ,
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

    function fetch_movies_list(page, search){
        _url = '/api/movies/tv/?page=' + page;
        _v = GetQueryString('v');
        _search = _v?'&v=' +  _v:'';
        _url = _url + _search;
        console.log(_url)
        $.ajax({
            url: _url ,
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
        $('#seq-list').empty();
        for(var i=0;i < items.length - 1; i=i+2){
            html =  '<div class="swiper-slide swiper-slide-active" style="width: 636px;">'+
                    '<ul class="clear">'+
                        '<li><a href="/movies/play/?v=' + items[i].url + '" target="_self">'+
                        '<em><span>' + items[i].seq + '</span>' + items[i].title + '</em></a></li>'+
                        '<li><a href="/movies/play/?v=' + items[i].url + '" target="_self">'+
                        '<em><span>' + items[i+1].seq + '</span>' + items[i+1].title + '</em></a></li>'+
                    '</ul>'+
                '</div>'+
            $('#seq-list').append(html)
        };
        if(items.length==0){
            $('#seq-list').append('<span style="color:black;">没有找到</span>')
        };

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

    $('#fa-search').on('click', function(){
        page_cur = 1;
        search_content = $('input[name="search"]').val();
        console.log(search_content);
        search(page_cur, search_content);
    });

    $('#searchinput').on('keypress', function(){
        page_cur = 1;
        search_content = $('input[name="search"]').val();
        console.log(search_content);
        search(page_cur, search_content);
    });

    fetch_page()

})
