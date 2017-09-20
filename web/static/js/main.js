

var fetch_movies_list = function(data){
    $.ajax({
        url: '/test',
        type: 'POST',
        data: '',
        success: function(data){
            console.log(data)
        },
        error: function(data){
            console.log('error')
        },
    });
};