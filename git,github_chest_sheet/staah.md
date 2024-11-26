# stash 
재 작업 중인 변경 사항을 임시로 저장하고 작업 디렉토리를 깨끗한 상태로 되돌리는 데 사용됩니다. 
이를 통해 다른 브랜치로 전환하거나 
긴급히 수정해야 할 작업을 처리한 뒤, 다시 원래 작업 상태로 돌아올 수 있습니다.
- git stash : 변경된 tracked 파일(Git에 추적 중인 파일)만 저장합니다.
(untracked(추적되지 않은) 파일이나 ignored(무시된) 파일은 기본적으로 저장되지 않습니다.)
- git stash -u   # Untracked 파일 포함
- git stash -a   # Ignored 파일 포함
  - git stash list : 저장된 스태시 목록을 확인합니다.
    -  stash@{0} : 0이 최신순 
  #### stash 복원
- git stash apply : 기본 복원 (저장 내용은 여전히 스태시에 남아 있음)
  - git stash pop : 복원 후 제거 (스태시 목록에서 제거)
  - git stash apply stash@{n} : 특정 스태시 복원
#### stash 삭
- git stash drop : 가장 최근의 스태시 제거
  - git stash drop stash@{n} : 특정 스태시 제거
  - git stash clear : 모든 스태시 삭제 
#### stash 설명
- git stash save "작업 설명" : 설명 추가
- git stash show stash@{n} : 요약 확인
- git stash show -p stash@{n} : 자세한 변경 사항 확인









