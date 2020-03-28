# 한양 플레이트 (한양대학교 주변 맛집 리뷰 사이트 만들어보기)

3.8 > python version >= 3.6

## 프로젝트 시작하기

- 가상환경 시작하기: `python3 -m venv [프로젝트 가상환경 이름]`

- 가상환경 활성화하기: `[프로젝트 가상환경 이름]\Scripts\activate`

- Django 설치하기: `pip3 install django==2.2.5`

- 프로젝트 시작하기: `django-admin startproject hanyang_plate`

- 기본 데이터베이스 만들기: `python3 manage.py migrate`

- 서버 실행하기: `python3 manage.py runserver`


## 어플리케이션 만들기

- 어플리케이션 만들기: `django-admin startapp [어플리케이션 이름]`
*보통 어플리케이션 이름은 복수형 명사, 스네이크 케이스로 정합니다*

- [프로젝트 이름]/urls.py 고치기

- [어플리케이션 이름]/urls.py 생성하기

- [프로젝트 이름]/settings.INSTALLED_APPS 에 [어플리케이션 이름] 추가
```python 
hanyang_plate/settings.py

...

INSTALLED_APP = [
  ...
  ...
  ...
  'posts'
]

...

```  

- [프로젝트 이름]/settings 의 template dir 에 [os.path.join(BASE_DIR, "templates")] 추가
```python 
hanyang_plate/settings.py

...


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

...

```  



```python
# hanyang_plate/urls.py

from django.urls import path, include

urlpatterns = [
  path("", include("posts.urls")),
]

```  

```python
# posts/views.py

def home(requests):
  return render(requests, "posts/home.html")

```  

```python
# posts/urls.py
from posts import views

urlpatterns = [
  path("", views.home)
]

```  

``` html
<!-- hanyang_plate
posts
|--templates
|--|--posts
|--|--|--home.html
manage.py
README.md
 -->

<!-- posts/templates/posts/home.html -->

<h1>홈입니다</h1>

```  
