```
def profile(request, pk):
    user = User.objects.get(pk=pk)
    boards = user.board_set.all()
    comments = user.comment_set.all()
    context = {
        'boards': boards,
        'comments': comments,
    }

    return render(request, 'accounts/profile.html', context)
```

**특정 사용자의 프로필 페이지 구현**
- URL로 전달받은 사용자 기본 키(pk)를 이용해 특정 사용자가 작성한 게시글과 댓글 조회 <br>
- 이를 컨텍스트에 담아 프로필 템플릿에 전달하여 사용자 프로필 페이지에 표시되도록 구성 

<br>

```
@login_required
def follow(request, user_pk) : 
    User = get_user_model()
    user = User.objects.get(pk = user_pk)
    if request.user in user.followers.all() : 
        user.followers.remove(request.user)
    else : 
        user.followers.add(request.user)
    return redirect('accounts:profile', user_pk)
```

**유저 팔로우 기능 구현**
- 로그인한 사용자만 접근할 수 있도록 @login_required 데코레이터를 사용 <br>
- user_pk로 해당 사용자를 조회하고, 현재 로그인 한 사용자가 이미 해당 사용자의  팔로워 목록에 있다면 언팔로우, 아니라면 팔로우 처리 <br>
- 처리 후 해당 사용자의 프로필 페이지로 리디렉션 <br>