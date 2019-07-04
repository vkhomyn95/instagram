// AJAX для комента
$(document).ready(function(){
    var commentForm = $('#form-comment-ajax');
    commentForm.submit(function(event){
        event.preventDefault();
        $.ajax({
            url: commentForm.attr('action'),
            method: commentForm.attr('method'),
            data: commentForm.serialize(),
            success : function(data){
                console.log(data)
                $(".block-to-be-refreshed").prepend('' +

                    '<p><strong>' + data["user"] + '</strong>' + ' ' + data["text"] + '</p>'

                );
                commentForm[0].reset();
            },
            error : function(data){
                alert(JSON.stringify(data.responseJSON.errors))
            }
        })
    });

    function generateUserList(users) {
        var userList = '';
        users.forEach(function(user){
            userList += '<li>' + user + '</li>'
        });
        return userList
    }

   var likeForm = $('.form-like-ajax');
   likeForm.submit(function(event){
       event.preventDefault();
       $.ajax({
           url: $(this).attr('action'),
           method: $(this).attr('method'),
           data: $(this).serialize(),
           dataType: "json",
           success : function(data){
               $('#total_likes_photo_id__' + data['photo_id']).text(data['total_likes']);
               $('#users_photo_id__' + data['photo_id']).html(generateUserList(data['users']));
               $('#button_like_photo_id__' + data['photo_id']).text(data['is_likes'] ? 'Dislike' : 'Like')
           },
           error : function(data){
               alert(data['statusText'] + ': ' + data['responseJSON']['errors'])
           }
       })
   })

//    $('#lazyLoadLink').on('click', function() {
//    var link = $(this);
//    var page = link.data('page');
//    $.ajax({
//      type: 'post',
//      url: '/lazy_load_posts/',
//      data: {
//        'photo': photo_id,
//        'page': page,
//        'csrfmiddlewaretoken': window.CSRF_TOKEN
//      },
//      success: function(data) {
//        console.log(data)
//        if (data.has_next) {
//            link.data('page', page+1);
//        } else {
//          link.hide();
//        }
//
//        $('#posts').append(data.posts_html);
//      },
//      error: function(xhr, status, error) {
//
//      }
//    });
//  });


//DetailView lazyload comments
size_li = $("#myList li").length;
x=5;
$('#myList li:lt('+x+')').show();
$('#loadMore').click(function () {
    x= (x+5 <= size_li) ? x+5 : size_li;
    $('#myList li:lt('+x+')').show();
});
$('#showLess').click(function () {
    x=(x-5<0) ? 3 : x-5;
    $('#myList li').not(':lt('+x+')').hide();
});


///////

var leadForm = $('.add-lead-form')
leadForm.submit(function(event){
       event.preventDefault();
       $.ajax({
           url: $(this).attr('action'),
           method: $(this).attr('method'),
           data: $(this).serialize(),
           dataType: "json",
           success : function(data){

           },
           error : function(data){
               alert(data['statusText'] + ': ' + data['responseJSON']['errors'])
           }
       })
   })


});
