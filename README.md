# Instagram_clonecoding_team8
인스타그램 클론 코딩 팀프로젝트입니다.

![GitHub last commit](https://img.shields.io/github/last-commit/grolarkim/Instagram_clonecoding_team8?style=plastic)

------------

# 인스타그램 클론 코딩

인스타그램을 클론 코딩하여 프론트엔드를 만들고, Flask와 MongoDB를 사용하여 서버까지 구현까지 하는 프로젝트입니다.

#### 8조 경수없는 경수팀

김명준(조장) : 기본페이지, EC2

이가을 : 로그인,회원가입 페이지 

이상호 : 프로필페이지

서로서로 도우면서 진행되었습니다.

------------
## 기능 및 구조


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


------------
## 결과 화면

1. 로그인 화면
> ![](https://images.velog.io/images/grolar812/post/42e1a528-d8f6-4f97-937f-0f972ea805c4/%EC%9D%B8%EC%8A%A4%ED%83%80%20%EB%A1%9C%EA%B7%B8%EC%9D%B8%20%EC%B0%BD.png)

2. 회원가입 화면
> ![](https://images.velog.io/images/grolar812/post/1bfb64fd-8be1-4443-af00-6cb8b5824a6d/%EC%9D%B8%EC%8A%A4%ED%83%80%20%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85%20%EC%B0%BD.png)

3. 기본화면
> ![](https://images.velog.io/images/grolar812/post/e342bc3d-b161-4749-b89e-1f2d49dfb2e7/%EC%9D%B8%EC%8A%A4%ED%83%80%20%EA%B8%B0%EB%B3%B8%20%ED%99%94%EB%A9%B4.png)

4. 프로필 화면
>
1 기본
![](https://images.velog.io/images/grolar812/post/04d2ae93-0678-46a1-ac1b-bab39d937f5e/%EC%9D%B8%EC%8A%A4%ED%83%80%20%ED%94%84%EB%A1%9C%ED%95%84%20%EC%B0%BD%201.png)
2 프로필 편집
![](https://images.velog.io/images/grolar812/post/5b045b9f-0246-4902-b403-46faab075896/%EC%9D%B8%EC%8A%A4%ED%83%80%20%ED%94%84%EB%A1%9C%ED%95%84%20%EC%B0%BD%202.png)

5. 게시물 생성 화면
> ![](https://images.velog.io/images/grolar812/post/cd67728f-ba51-4d29-a3b0-53c7da6bd7e6/%EC%9D%B8%EC%8A%A4%ED%83%80%20%EA%B2%8C%EC%8B%9C%EB%AC%BC%20%EC%83%9D%EC%84%B1%20%EC%B0%BD.png)

