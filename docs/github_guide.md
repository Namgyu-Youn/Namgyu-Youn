**Github Issue, PR(Pull Request) 사용법**
=====================================

- 이 문서는 Github의 Issue, PR(Pull Request)에 대한 소개와 사용법에 대해서 다룹니다.
- Github에서 Issue, Issue branch, PR은 하나의 묶음이라고 볼 수 있습니다.
- Issue는 작업할 내용을 기록하기 위해서 사용되고, PR은 작업한 내용을 main branch에 commit(merge)하기 위해서 사용됩니다.
- Github branch를 분리함으로써 "팀원 간의 작업 환경 분리"를 하고, 이를 통해서 체계적인 source control을 경험할 수 있습니다.
- Bug-Hotfix가 아닌 경우에는 main branch commit은 금지되며, 모든 작업은 Issue branch에서 진행되어야 합니다.

### **0. Issue 생성하기**
- Github Issue는 "작업할 내용"을 기록하기 위해서 사용됩니다.
- "Github Repository -> Issues -> New Issues"를 통해서, 새로운 Issue 생성이 가능합니다.
- Issue에는 Background(작업을 소개하는 내용), Todo(작업할 내용), See also(참고할 내용), Assignees(작업하는 팀원 지정), Labels(이슈의 목적) 등을 이용해서 자세하게 기록할 수 있습니다.
- Issue를 생성하면, branch를 생성할 수 있으며 모든 작업은 해당 branch에서 진행됩니다.
![{16872E61-85DC-4164-89BA-837B5188C037}](https://github.com/user-attachments/assets/f5f5ee56-30f3-438c-8fc2-7a1871aaf9ef)

### 1. Issue에서 생성한 branch로 이동하기
Step 1. F1 -> git clone -> Repository URL 입력
- 순차적으로 실행했을 때 결과는 아래와 같습니다.
![{DAF6C39B-9942-4FAF-AA43-0D381B005327}](https://github.com/user-attachments/assets/276d51b5-37de-4e78-b9b8-92cd3b20b8e5)

Step 2. F1 -> git fetch
- git fetch는 branch 목록들을 동기화 해주는 명령어 입니다.
- 이를 입력하면 main branch 뿐만 아니라, 다른 branch들의 변경 사항들도 확인할 수 있습니다.
![{6FB0F38E-1BFB-4166-B3BE-309060071286}](https://github.com/user-attachments/assets/d2ed8b81-b2d9-42fc-9471-4828c47a64ee)

Step 3. F1 -> git checkout -> branch 이름 입력
- git checkout은 branch를 변경하는 명령어 입니다.
- git checkout을 입력하면, 원격으로 접속 가능한 branch들이 조회되며 작업할 branch를 선택할 수 있습니다.

![{120C30A7-8535-4CA9-B855-FE9016C499EF}](https://github.com/user-attachments/assets/4934889d-ffcf-4510-aa92-b5a4e704ccfc)


### 4. Issue branch에서 작업하기.
- 이동한 branch에서 작업 합니다.
- 작업한 내용은 Issue를 통해 생성된 branch에서 commit하면서 기록합니다.


### **5. PR(Pull-Request) 생성하기**
- PR은 작업이 끝난 내용을 main branch에 merge(병합)하기 위해 필요합니다.
- "Github Repository -> Pull Request -> New pull request"를 통해서 새로운 PR 생성이 가능합니다.
![{F741F728-D8B4-427B-B32E-489464F9C273}](https://github.com/user-attachments/assets/ac0191be-7cc6-4047-84fb-d72e700b222a)
- 생성한 PR의 예시는 아래와 같습니다.
- PR에는 Overview(작업한 내용), Issue Tags(작업한 Issue) 등을 이용해서 자세하게 기록할 수 있습니다.
- Issue Tags에서 "Closed | Fixed" 부분에 "#(Issue 번호)"를 입력하면, 해당 Issue가 자동으로 Close 됩니다.

![{3D050E84-0479-4B66-9E1F-B59A54FDC207}](https://github.com/user-attachments/assets/059f2f0e-492d-45af-b5d2-35a0e9c9caab)
---

### (Optional) VScode에서 모든 것을 제어하기
- 이전 과정을 통해서 Issue, PR에 익숙해졌다면 VScode Extension인 "GitHub Pull Requests"를 사용해서 모든 내용을 VScode 안에서 시도할 수 있습니다.
- 또한 branch를 생성하면 "Commit graph"를 통해서 Source view & control이 가능합니다.

![{9BF83DA5-BBF0-4762-968A-EE933F5BDF15}](https://github.com/user-attachments/assets/3e004a02-442c-4528-9a96-a18c4659dd76)
