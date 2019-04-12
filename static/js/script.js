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

    $('#lazyLoadLink').on('click', function() {
    var link = $(this);
    var page = link.data('page');
    $.ajax({
      type: 'post',
      url: '/lazy_load_posts/',
      data: {
        'page': page,
        'csrfmiddlewaretoken': window.CSRF_TOKEN // from index.html
      },
      success: function(data) {
        console.log(data)
        if (data.has_next) {
            link.data('page', page+1);
        } else {
          link.hide();
        }

        $('#posts').append(data.posts_html);
      },
      error: function(xhr, status, error) {

      }
    });
  });


});
