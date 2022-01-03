$(document).ready(function () {
    show_me();
    show_pic();
});
function open_box() {
    $('#edit-container').show()
}
function close_box() {
    $('#edit-container').hide()
}
function show_me() {
    $.ajax({
        type: 'GET',
        url: '/api/my_post',
        data: {},
        success: function (response) {
            let name = response['user_infos'][0]['name']
            let desc = response['user_infos'][0]['desc']
            let url = response['user_infos'][0]['url']
            let id = response['user_infos'][0]['id']
            let post_count = response['post_list'].length
            let mini_profile_html = `<a href="/profile" class="icons" id="profile_pc" style="background: url('${url}') no-repeat;background-position: center; background-size: cover;""></a>`
            $('#head_leftside').append(mini_profile_html)
            let info_html = `<div class="profile_img">
                                    <img src="${url}" alt="">
                                </div>
                                <div class="info">
                                    <div class="area_text">
                                        <h2 class="user_id">${name}</h2>
                                        <button onclick ="open_box()" class="profile_edit">프로필 편집</button>
                                        <button type="button" class="setting_btn">
                                            <i class="fas fa-cog"></i>
                                        </button>
                                    </div>
                                    <div class="area_text">
                                        <div class="tit_desc">
                                            <span class="title">게시물</span>
                                            <span class="sub_title">${post_count}</span>
                                        </div>
                                        <div class="tit_desc">
                                            <span class="title">팔로워</span>
                                            <span class="sub_title">0</span>
                                        </div>
                                        <div class="tit_desc">
                                            <span class="title">팔로우</span>
                                            <span class="sub_title">0</span>
                                        </div>
                                    </div>
                                    <div class="area_text profile_info">
                                        <h3 class="info_title">${id}</h3>
                                        <p class="info_sub">${desc}</p>
                                    </div>
                                </div>
                            </div>`
            $('#profile').append(info_html)
        }
    })
}
function show_pic() {
    $.ajax({
        type: 'GET',
        url: '/api/my_post',
        data: {},
        success: function (response) {
            let rows = response['post_list']
            for (i = 0; i < rows.length; i++) {
                let pic = rows[i]['url']
                let pic_html = `<ul class="board_list">
                                    <li>
                                        <a href="">
                                            <div class="board_img">
                                                <img src="${pic}" alt="배경 이미지">
                                            </div>
                                        </a>
                                    </li>
                                </ul>`
                $('#photos').append(pic_html)
            }
        }
    })
}
function Update_profile() {
    let rename = $('#name-change').val()
    let redesc = $('#desc-change').val()
    let reurl = $('#url-change').val()
    $.ajax({
        type: 'POST',
        url: '/api/profile_update',
        data: {name_give : rename, desc_give: redesc, url_give : reurl},
        success: function (response) {
            alert(response['msg'])
            window.location.reload()
        }
    })
}