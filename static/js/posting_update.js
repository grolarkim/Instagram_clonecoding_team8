function post_update() {
    let url = $('#url').val()
    let desc = $('#desc').val()
    let time = $('#posting_btn').val()

    $.ajax({
        type: 'POST',
        url: '/api/post_update',
        data: {url_give : url, desc_give : desc, time_give : time},//아이디,사진url,소개
        success: function (response) {//반환잘받으면
            alert(response['msg'])
            window.location.href = "/";
        }
    })
}