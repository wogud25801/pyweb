from django.urls import path
from . import views
from board.views import base_views, question_views, answer_viewes, vote_views,comment_views

app_name = 'board'  #네임 스페이스(소속) - url경로 이름

urlpatterns = [
    # 인덱스 페이지
    path('', base_views.index, name='index'),  #127.0.0.1:8000/board/
    # 질문 목록
    path('boardlist/', base_views.boardlist, name='boardlist'),  #127.0.0.1:8000/board/
    # 상세 페이지
    path('<int:question_id>/', base_views.detail, name='detail'), #127.0.0.1:8000/board/1/
    # 질문 등록 - 127.0.0.1:8000/board/question/create/
    path('question/create/', question_views.question_create, name='question_create'),
    # 답변 등록 - 127.0.0.1:8000/board/answer/create/1/
    path('answer/create/<int:question_id>/', answer_viewes.answer_create, name='answer_create'),
    # 질문 수정
    path('question/modify/<int:question_id>/', question_views.question_modify, name='question_modify'),
    # 답변 수정
    path('answer/modify/<int:answer_id>/', answer_viewes.answer_modify, name='answer_modify'),
    # 질문 삭제
    path('question/delete/<int:question_id>/', question_views.question_delete, name='question_delete'),
    # 답변 삭제
    path('answer/delete/<int:answer_id>/', answer_viewes.answer_delete, name='answer_delete'),
    # 질문 추천
    path('vote/question/<int:question_id>/', vote_views.vote_question, name='vote_question'),
    # 댓글 등록
    path('comment/create/question/<int:question_id>/', comment_views.comment_create_question,
         name='comment_create_question'),
]