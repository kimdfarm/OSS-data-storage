# 파일 상태 보여주기

### 1. git status : 현재 Git 저장소의 상태를 보여주는 명령어입니다. 이 명령어를 사용하면, 작업 디렉토리와 스테이징 영역(stage)에서 어떤 변경이 있었는지 확인할 수 있습니다. 
<br>

- git status :             기본적인 브랜치 상대와 변경된 파일들을 보여준다.
  - git status -u :        추적되지 않는 파일을 보여주는 옵션이다. 즉 파일에 적은 파일을 add, commit 하지 않는 파일들까지 알려준다.
  - git status -u no :     추적되지 않은 파일을 표시하지 않습니다.
  - git status -u normal : 기본적으로 추적되지 않은 파일을 보여줍니다 (기본 설정).
  - git status -u all: 모든 추적되지 않은 파일을 상세히 나열합니다.
- git status -s
- git status --short
  이 옵션은 간략한 출력을 제공하여, 스테이징된 파일과 수정된 파일의 상태를 짧고 간단하게 보여줍니다.
  <br>
   
  - !	: 무시됨        (Ignored)
  - A : 추가됨        (added)
  - M : 수정됨        (modified)
  - D : 삭제됨        (deleted)
  - R	: 이름 변경됨    (Renamed)
  - C	: 복사됨         (Copied)
  - ?	: 추적되지 않음  (Untracked)
  - !	: 무시됨         (Ignored)
 <br>
 
  git config --global color.status.(파일 상태 영어) "rgb:0,0,0" : 특정 상태의 색상 사용자 지정  
    <br>
    ##### 기본 (default)
    - 초록색 (green)	:   새로 추가된 파일이 스테이징됨.
    - 노란색 (yellow) :  기존 파일이 수정됨.
    - 빨간색 (red)	      파일이 삭제됨.
    - 빨간색 (red bold)	Git이 추적하지 않는 새 파일.
    - 회색 (gray)	     .gitignore에 의해 무시되는 파일.
 
