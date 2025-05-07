# 개인별 관심 종목 관리 기능 구현 보고서 (코드 주요 기능 요약 및 설명)

## 회원가입
```
@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('contentfetch:stock_finder')

    form = CustomUserCreationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        # 자동 로그인 원할 경우 다음 줄 추가:
        auth_login(request, user)
        return redirect('contentfetch:stock_finder')

    return render(request, 'accounts/signup.html', {'form': form})
```
- auth_login(request, user): 회원가입 후 자동 로그인 기능 

## 로그인 및 로그아웃
```
@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('contentfetch:stock_finder')

    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        auth_login(request, form.get_user())
        return redirect('contentfetch:stock_finder')

    return render(request, 'accounts/login.html', {'form': form})
```

```
@login_required
@require_POST
def logout(request):
    auth_logout(request)
    return redirect('contentfetch:stock_finder')
```
- 로그인된 사용자는 접근 불가 → 메인 페이지로 이동
- POST 방식으로만 유효성 검증 후 로그인 및 로그아웃 가능


## 관심 종목 관리 기능 구현
```
@require_safe
def detail(request, user_pk):
    user = User.objects.get(pk=user_pk)
    favorites = user.favorites.all()
    return render(request, 'accounts/detail.html', {'favorites': favorites})
```
- @require_safe: 안전한 요청(GET/HEAD)만 허용
- 해당 유저의 관심 종목 관리 및 조회

```
@login_required
@require_POST
def addfavorites(request):
    company_name = request.POST.get('company_name')
    if company_name and not Favorite.objects.filter(user=request.user, company_name=company_name).exists():
        Favorite.objects.create(user=request.user, company_name=company_name)
    return redirect('accounts:detail', request.user.pk)
```
- 로그인한 사용자만 즐겨찾기 항목을 추가 가능
- 중복된 항목을 추가하지 않도록 체크
- @require_POST: POST 요청만 처리하여 데이터의 안전성을 확보