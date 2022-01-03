function posting() {
    let id = $('#posting_btn').val()
    let url = $('#url').val()
    let desc = $('#desc').val()
    let d = new Date()
    let time = d.getTime()

    $.ajax({
        type: 'POST',
        url: '/api/posting',
        data: {id_give : id, url_give : url, desc_give : desc, time_give : time},//아이디,사진url,소개
        success: function (response) {//반환잘받으면
            alert(response['msg'])
            window.location.href = "/";
        }
    })
}