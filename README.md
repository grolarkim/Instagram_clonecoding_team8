# Instagram_clonecoding_team8
인스타그램 클론 코딩 팀프로젝트입니다.

![GitHub last commit](https://img.shields.io/github/last-commit/grolarkim/Instagram_clonecoding_team8?style=plastic)

------------

# 인스타그램 클론 코딩

인스타그램을 클론 코딩하여 프론트엔드를 만들고, Flask와 MongoDB를 사용하여 서버까지 구현까지 하는 프로젝트입니다.

#### 8조 경수없는 경수팀
김명준(조장):백엔드,EC2
김경은: 프론트엔드
이가을:프론트엔드
이상호:백엔드


------------

## 와이어 프레임
크게 3종류의 페이지를 만들 것이고, 팝업이나 모달 창을 통하여 추가 기능의 구현을 예정

#### 기본 페이지
인스타그램의 포스트를 볼 수 있는 페이지, 기존 과제의 페이지에서 제작 예정
> ![](https://images.velog.io/images/grolar812/post/8d2a2fee-e460-4fc4-8962-210d4f1779fb/image.png)

#### 개인 페이지
특정 인물의 프로필과 포스트를 볼 수 있는 페이지, 본인의 경우 북마크한 페이지 표시
> ![](https://images.velog.io/images/grolar812/post/a3348836-f746-483e-b756-a54334b0e21b/image.png)

#### 로그인 페이지
로그인을 할 수 있는 페이지, 다른 페이지에서 로그아웃 시 도달할 페이지
> ![](https://images.velog.io/images/grolar812/post/c54cc3aa-c121-4e0e-892b-385f65bc5591/image.png)


------------

## 기능 및 DB구조 설계

### 기능 설계
요약본

| NO. | 기능 | 요청방식 | url | request (프론트에서 ajax 사용시 data에 넣을 것) | response (백엔드에서 jsonify 사용시 넣을것) | 비고 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 메인화면 | GET | / |  |  | (index.html불러옴) |
| 2 | 메인화면 데이터보내기 | POST | /api/timeline | {id_give: id} | {'post':post_list}  | DB에서 ID가 같은 작성글 검색 |
| 3 | 마이 페이지 | GET | /profile |  |  | (profile.html불러옴) |
| 4 | 마이 페이지 데이터 보내기 | POST | /api/my_post | {id_give: id} | {'post':post_list} | DB에서 ID가 같은 작성글 검색 |
| 5 | 로그인 페이지 | GET | /login |  |  | (login.html불러옴) |
| 6 | 로그인 | POST | /api/login | {id_give : id ,pw_give : pw}  | 성공시 {'result': 'success', 'token': token} 실패시 {'result': 'fail', 'msg': '아이디/비밀번호가 일치하지 않습니다.'} | DB에 있는지 검색 후 있으면 로그인 |
| 7 | 회원가입 창 | GET | /register |  |  | (register.html불러옴) |
| 8 | 계정생성 | POST | /api/register | {id_give : id , pw_give :pw, url_give :url,   name_give:name, desc_give: desc} | {'result': 'success'} | 중복 ID 검색후 없으면 DB에 저장 |
| 9 | 게시글 올리기 페이지 | GET | /posting |  |  | (posting.html불러옴) |
| 10 | 게시글 올리기 | POST | /api/posting | {post_img_give: post_img, post_text_give: post_text, author_id_give: author_id, post_time_give: post_time} | {'result': 'success'} | DB에 저장 |


#### 0. 기본 기능
헤드에 있는 버튼들 기능 구현 _(3~5가지 기능)_

- 인스타 로고 - 홈으로
- 검색 - (옵션)
- 홈 - 홈으로
- 디엠 - (옵션)
- 게시물추가 - 팝업으로
- 트렌드 - (옵션)
- 하트 - (옵션)
- 계정-설정 - 계정 정보페이지 (옵션?필수?)

#### 1. 홈 - 피드 추천 등 과제떄 사용한 페이지

1. 페이지 읽어오기 _(2~4가지 기능)_
 - 포스트 불러오기(R)
 - 로그인 되어있는 사람 정보(R)
 - 스토리 불러오기(R, 옵션)
 - 팔로우 추천(R, 옵션)        

2. 포스트 단독 보기 _(모달창 사용, 3~4가지 기능)_
 - 좋아요(U)
 - 북마크(U)
 - 댓글(C,U)
 - 신고 등(옵션)

#### 2. 로그인
로그인 페이지 _(2가지 기능)_
 - 로그인
 - 로그아웃
 - JWT사용 
 
 - 계정전환없이 로그아웃(옵션 1) 
 - 계정 전환 등 팝업 로그인(옵션 2)
 
####  3. 게시물 추가
팝업(modal), 페이지 중 하나 _(1~ 기능,옵션에 따라 기능 개수 변화)_
 - 이미지, 동영상 등을 첨부하여 게시물 만들기 (C)
 - 옵션(이미지 자르기, 필터, 조정 등)
 
####  4. 내 페이지, 5. 다른사람 페이지
개인 페이지 제작, 내 페이지의 경우 북마크 탭 추가 _(가능한 한번에 많은 정보 불러오기, 3~4 기능)_
 - 프로필 사진 (R)
 - 프로필 설명 (R)
 - 팔로우, 팔로워 수 (R)
 - 게시물 - 게시한 것 표시 (R)
 - 저장됨 - 북마크한 것 표시 (R)
 - 포스트 삭제 기능 (D) 
 - 태그됨 - 옵션


### DB구조 설계

#### 1. 계정 정보 데이터 베이스
 - 아이디
 - 비밀번호
 - 프로필 사진
 - 프로필 설명
 - 북마크(url만)
 - 포스트(url만)
 - 팔로우 (이름, 인원 수, 옵션)
 - 팔로워 (이름, 인원 수, 옵션)


#### 2. 포스트 데이터 베이스
- 작성자
- 사진이나 동영상(데이터베이스에 직접?, url만?)
- 좋아요(수, 누가했는지)
- 댓글(누가, 어떤내용)
- 작성시각

