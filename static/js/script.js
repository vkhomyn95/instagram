// AJAX для комента
$(document).ready(function(){
    var commentForm = $('.form-comment-ajax')
    commentForm.submit(function(event){
        event.preventDefault();
        var thisForm = $(this)
        var actionPoint = thisForm.attr('action');
        var httpMethod = thisForm.attr('method');
        $.ajax({
            url: actionPoint,
            method: httpMethod,
            data: {csrfmiddlewaretoken:'{{csrf_token}}' },
            success : function(data){
                $(".block-to-be-refreshed").load(" .block-to-be-refreshed");
                console.log('success')
                console.log(data)
            },
            error : function(errorData){
                console.log('error')
                console.log(errorData)
            }
        })
    })
//    var likeForm = $('.form-like-ajax')
//    commentForm.submit(function(event){
//        event.preventDefault();
//        var thisForm = $(this)
//        var httpMethod = thisForm.attr('method');
//        $.ajax({
//            url: "{% url 'like_photo' %}",
//            method: httpMethod,
//            data: {'id': $(this).attr('value'), 'csrfmiddlewaretoken': '{{ csrf_token }}'},
//            dataType: "json",
//            success : function(data){
//
//                console.log('success2222')
//                console.log(data)
//            },
//            error : function(errorData){
//                console.log('error')
//                console.log(errorData)
//            }
//        })
//    })
})