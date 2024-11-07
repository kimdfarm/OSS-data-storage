## git을 깔고 먼저 적어야 할 코드는 무엇인가?

### git init
#### git 저장소를 초기화 한다.
<br>
<br>



# git config --(설정범위) (설정변수) (저장값) <br>
## 설정범위 <br>
### | --system | --global | --local | <br>
- --system일 경우 모든 사용자에게 적용됨으로 잘 사용되지 않는다.
- --global은 현재 사용자의 모든 저장소에 사용됨으로 한번 사용하고 모든 저장소에 저장된다.
- --local일 경우 현재 저장소에서만 저장되여 다른 저장소에서 사용할떄 계속 설정변수를 넣어야 한다.

## 설정변수와 저장값
### core.editor 
- commit할 때 메세지를 설정할 수 있다.<br> 
- 기본적으로 Vim으로 설정되여 있다<br> 
- 모든 편집기 안에 <br> 
Please enter the commit message for your changes. Lines starting with '#' will be ignored,<br>
 and an empty message aborts the commit. 이 있으며<br>

- 그 내용은 <br>
변경 사항에 대한 커밋 메시지를 입력하세요. '#'로 시작하는 줄은
무시되고, 빈 메시지는 커밋을 중단합니다.<br>

### vim 
- 기본 편집기로 git commit할 때 나타난다.<br>
나오면 당황스럽습니다.

1. 침착하게 i을 눌러 커밋할 내용을 적습니다.

- #안에 적지 마시오
  
3. 다 적었으면 Esc을 누룹니다.
4. :wq을 누르고 Enter 치면 커밋됩니다.

#### 만약 편집기 안에 고유적인 말이 없고 갑자기 오류가 뜬다
밑으로 내려가다보면 
이 6가지 경우로 나타낸다.

- (O)pen Read-Only: 파일을 읽기 전용 모드로 엽니다. 이 경우 편집은 할 수 없지만 내용을 확인할 수 있습니다
- (E)dit anyway: 편집을 강행합니다. 이는 다른 프로그램에서 같은 파일을 열었을 가능성이 있는 경우 충돌이 발생할 수 있어 주의가 필요합니다.
- (R)ecover: 편집 중인 파일의 복구 기능을 사용합니다. Vim은 파일을 자동으로 백업하므로 작업 중이던 내용을 복구할 수 있습니다.
- (D)elete it: .swp 파일을 삭제하여 이 메시지를 제거합니다. 다른 편집 세션이 이미 닫혀 있다면, 이 옵션을 사용하여 안전하게 작업을 이어갈 수 있습니다.
- (Q)uit: Vim을 종료하고 아무 작업도 수행하지 않습니다.
- (A)bort: Vim을 종료하고 실행을 중지합니다.

추천 (R)ecover, (D)elete it
무한반복 (비추천) (O)pen Read-Only, (Q)uit, (A)bort






