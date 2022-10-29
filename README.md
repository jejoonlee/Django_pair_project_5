
# 💬 하그스랜드

🔗 [배포 URL](https://www.google.co.kr/)

## 개요

- 🎠 하그스랜드는 하이퍼그로스 강사님들에게 응원 & 감사의 댓글을 남길 수 있는 서비스입니다.
- 🔮 글과 사진과 함께 댓글을 작성하여 자신의 생각을 공유할 수 있습니다.
- 💖 피드를 구경하다가 마음에 드는 댓글을 발견한다면 좋아요를 남길 수 있습니다.
- ❌ 비방글은 바로 삭제됩니다.

## 멤버 구성

- 🙋‍♂️ 이제준 🔗 [github/jejoonlee](https://github.com/jejoonlee)
- 🙋🏻‍♂️ 장성민 🔗 [github/min486](https://github.com/min486)

<hr>

## 프로젝트 결과

gif

## 프로젝트 구조

- login.html : 로그인 페이지를 기본 홈 url로 설정(' ')
- index.html : 로그인 후 나타나는 페이지, 게시글 목록
- review.html : 댓글 목록 (+ 댓글 좋아요, 팔로우)

```
│  README.md
├── base
│    └── base.html
├── static\css
│    └── style.css
├── accounts
│    ├── templates
│    │    ├── login.html
│    │    └── signup.html
│    ├── urls.py
│    └── views.py
├── articles
│    ├── templates
│    │    ├── index.html
│    │    └── review.html
│    ├── urls.py
│    └── views.py
└── pair_project
     ├── settings.py
     └── urls.py
```

