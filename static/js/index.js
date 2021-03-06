$(document).ready(function () {
    show_story();
    show_post();
    show_recommend();
});

function show_story() {
    $.ajax({
        type: 'GET',
        url: '/api/timeline',
        data: {},
        success: function (response) {
            let url = response['user_infos'][0]['url']
            let name = response['user_infos'][0]['name']
            let story_html = `<div class="story_wrap">
                <div class="story_pic" style="background: url('${url}') no-repeat;background-position: center; background-size: cover;">

                </div>
                <p class="story_name">
                    ${name}
                </p>

            </div>`
            $('#my_story').append(story_html)
            //마이페이지로 가는 버튼을 프로필사진으로 불러올 수 있도록 바꿨습니다.
            let mini_profile_html = `<a href="/profile" class="icons" id="profile_pc" style="background: url('${url}') no-repeat;background-position: center; background-size: cover;""></a>`
            $('#head_leftside').append(mini_profile_html)
        }

    })
}

function show_post() {
    let d = new Date()
    time_now = d.getTime()
    time_now *= 1
    $.ajax({
        type: 'GET',
        url: '/api/timeline',
        data: {},
        success: function (response) {
            let url = response['user_infos'][0]['url']
            let name = response['user_infos'][0]['name']
            if (response['post_list'].length == 0) {
                let temp_post = `
                <button onclick="location.href='/posting'" class="need_new_posting">
                    <p>게시물이 없어요.</p>
                    <p class="new_po">새 게시물 생성하기</p>
                </button>
                `
                $('#my_post').append(temp_post)
            } else {
                for (let i = 0; i < response['post_list'].length; i++) {
                    let post = response['post_list'][i]['url']
                    let post_time = response['post_list'][i]['time']
                    let desc = response['post_list'][i]['desc']
                    let id = response['user_infos'][0]['id']
                    let time = time_now - post_time
                    let minute = parseInt(time / 60000)
                    let t
                    if (minute < 60) {
                        t = String(minute) + "분 전"
                    } else if (minute < 1440) {
                        t = String(parseInt(minute/60)) + "시간 전"
                    } else if (minute < 43200) {
                        t = String(parseInt(minute/1440)) + "일 전"
                    } else if (minute < 525600) {
                        t = String(parseInt(minute/43200)) + "달 전"
                    } else {
                        t = String(parseInt(minute/525600)) + "년 전"
                    }
                    let post_html = `<div class="post_container" >
                                        <div class="post_head">
                                            <div class="post_title" >
                                                <div class="title_pic" style="background: url('${url}') no-repeat;background-position: center; background-size: cover;">
                                                </div>
                                                <p class="title_name">
                                                    ${name}
                                                </p>
                                            </div>
                                            <button class="icon more" onclick="show_modal(modal_${post_time})">
                                            </button>
                                        </div>
                                        <div class="post_pic" style="background: url('${post}') no-repeat;background-position: center; background-size: cover;">
                                        </div>
                                        <div class="post_wrap">
                                            <div class="pic_desc">
                                                <p>${desc}</p>
                                            </div>
                                            <div class="time">
                                                    <p> ${t} </p>
                                            </div>
                                        </div>
                                        <div class="ud_modal" id="modal_${post_time}">
                                            <div class="ud_modal_window">
                                                <button onclick="location.href='/post_update?time=${post_time}'">게시물 수정</button>
                                                <button onclick="post_delete(${post_time})">게시물 삭제</button>
                                                <button onclick="close_modal()">닫기</button>
                                            </div>
                                        </div>
                                    </div>`
                    $('#my_post').append(post_html)
                }
            }
        }
    })
}

function post_delete(time) {
    if (confirm("이 게시물을 삭제하시겠습니까?")) {
        $.ajax({
            type: 'POST',
            url: '/api/post_delete',
            data: {time_give : time},
            success: function (response) {
                alert(response['msg'])
                window.location.reload();
            }
        })
    } else {
        alert("취소되었습니다.")
    }
                
}

function show_recommend() {
    $.ajax({
        type: 'GET',
        url: '/api/recommend',
        data: {},
        success: function (response) {
            let r_list = response['list']
            let list_leng = 0
            if (r_list.length < 5) {
                list_leng = r_list.length
            } else {
                list_leng = 5
            }
            for (let i = 0; i < list_leng; i++) {
                let name = r_list[i]['name']
                let url = r_list[i]['url']
                let desc = r_list[i]['desc']
                let temp_aside = `
                    <div class="aside_reco">
                        <div class="aside_user">
                            <div class="aside_pic" style="background: url(${url}) no-repeat; background-position: center; background-size: cover;">
                            </div>
                            <div class="aside_user_info">
                                <p><span>${name}</span></p>
                                <p>${desc}</p>
                            </div>
                        </div>
                        <div>
                            <a href="" class="aside_follow"></a>
                        </div>
                    </div>
                `
                $('#aside_wrapper').append(temp_aside)
            }

            
            
        }

    })
}

function show_modal(modal_id) {
    $(modal_id).show();
    $('html').css("overflow", "hidden");

}

function close_modal() {
    $('.ud_modal').hide();
    $('html').css("overflow", "auto");
}
