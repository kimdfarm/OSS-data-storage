# git을 깔고 먼저 적어야 할 코드는 무엇인가?

### git init
#### git 저장소를 초기화 한다.

## git config --(설정범위) (설정변수) (저장값)

# 설정범위
## | --system | --global | --local |
- --system일 경우 모든 사용자에게 적용됨으로 잘 사용되지 않는다.
- --global은 현재 사용자의 모든 저장소에 사용됨으로 한번 사용하고 모든 저장소에 저장된다.
- --local일 경우 현재 저장소에서만 저장되여 다른 저장소에서 사용할떄 계속 설정변수를 넣어야 한다.

# 설정변수와 저장값
## core.editor 
- commit할 때 메세지를 설정할 수 있다.<br> 
- 기본적으로 Vim으로 설정되여 있다<br> 
- 모든 편집기 안에 <br> 
Please enter the commit message for your changes. Lines starting
with '#' will be ignored, and an empty message aborts the commit.
이 있으며<br>
- 그 내용은 <br>
변경 사항에 대한 커밋 메시지를 입력하세요. '#'로 시작하는 줄은
무시되고, 빈 메시지는 커밋을 중단합니다.
이다
-vim
기본 편집기로 git commit할 때 나타난다.

