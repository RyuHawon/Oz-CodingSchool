from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def signup(request):
    # POST 요청일 경우 (회원가입 정보 제출 시)
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # 회원가입 성공 시 로그인 페이지로 이동
            # 'login'은 django.contrib.auth.urls에 기본적으로 포함된 URL 이름입니다.
            return redirect('login')
        # 폼이 유효하지 않으면, 아래의 render로 넘어가
        # 오류 메시지가 포함된 form 객체를 템플릿에 전달합니다.
    
    # GET 요청일 경우 (회원가입 페이지 첫 방문 시)
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'registration/signup.html', context)
