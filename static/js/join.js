function join() {
    let id = $('#id').val()
    let pw = $('#pw').val()
    let url = $('#url').val()
    let name = $('#name').val()
    let desc = $('#desc').val()

    $.ajax({
        type: 'POST',
        url: '/api/register',
        data: {id_give : id, pw_give : pw, url_give : url, name_give : name, desc_give : desc},//아이디,비밀번호,사진url,사용자이름,소개
        success: function (response) {//반환잘받으면
            alert(response['msg'])
            window.location.href = '/login'
        }
    })
}