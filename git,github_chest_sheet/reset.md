# reset
특정 커밋 상태로 현재 작업 트리와 인덱스(staging area)를 되돌리는 명령어입니다.
일반적으로 reset은 프로젝트의 상태를 수정하거나 정리할 때 사용됩니다.
- git reset : 인덱스에서 파일 제거, 작업 파일은 그대로 유지

###  --hard
- HEAD를 이동시키고, 인덱스와 작업 트리를 모두 되돌립니다. (되돌려진 변경 내용은 복구할 수 없음)
git reset --hard <커밋> : 해당 커밋 상태로 모든 것을 되돌림
### --mixed (기본 옵션)
 HEAD를 이동시키고, 인덱스를 초기화(staging area에서 제거)하지만, 작업 트리는 변경되지 않습니다.
- git reset --mixed <커밋>
### --soft
HEAD(현재 커밋 포인터)를 이동시키지만, 인덱스와 작업 트리는 변경되지 않습니다.
- git reset --soft <커밋>



