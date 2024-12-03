# revert
it에서 사용되는 명령어로, 커밋을 되돌리는 작업을 수행합니다. 
그러나 되돌리는 방식은 git reset과는 다릅니다.
- git revert는 새로운 커밋을 생성하여 이전 커밋의 변경 내용을 반대로 적용합니다.
- 히스토리를 보존하면서 특정 변경 사항만 되돌릴 수 있기 때문에, 협업 환경에서 안전하게 사용됩니다.
- 되돌린 결과를 작업 트리에 반영하고, 이를 커밋으로 남기기 때문에 로그 상에서도 변경 내역이 명확히 남습니다.

<br><br><br>


- git revert <커밋 해시>
  - <커밋 해시>는 되돌리고자 하는 커밋의 해시 값입니다.
  - 이 명령은 지정된 커밋의 내용을 반영 취소한 새로운 커밋을 생성합니다.
- git revert <시작 해시>..<끝 해시>
  - 범위를 지정하여 여러 커밋을 되돌릴 수 있습니다.
  - 하지만 이 경우 -n 옵션을 사용해 병합된 결과를 수동으로 확인하고 커밋하는 것이 일반적입니다.
- git revert --no-commit <커밋 해시>
  - 새로운 커밋을 바로 생성하지 않고, 변경 사항만 반영합니다.
  - 이 후 커밋 메시지를 수동으로 작성할 수 있습니다.
- git revert --continue : 되돌리는 과정에서 충돌이 발생하면, 충돌 내용을 수동으로 수정한 후에 커밋을 완료해야 합니다







