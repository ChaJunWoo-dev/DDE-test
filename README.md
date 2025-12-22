# DDE-test

## 주요 기능

- 게시글 작성, 조회, 수정, 삭제
- SQLite 데이터베이스 연동
- QStackedWidget 기반 페이지 전환
- Signal-Slot방식 이벤트 처리
- 게시글 작성/수정 시 공란 검증 및 QMessageBox기반 안내 메시지 표시
- 삭제 시 QMessageBox기반 삭제 확인 메시지 표시
- 게시글 최초 작성 시에는 작성일만 표시하고, 수정이 발생한 경우에만 수정일을 표시

## 사용 기술

- Python
- PySide6 - Qt GUI 프레임워크
- Pytz - 시간대 처리
- Pytest - 유닛 테스트
- SQLite - 데이터베이스

## 프로젝트 구조

화면, 데이터, 흐름 제어를 분리하는 형태로 구조를 설계했습니다. 

- db/  
  데이터베이스 접근 로직 담당


- models/  
  DB에서 조회한 데이터를 객체로 관리하고
  Qt의 Model 역할(TableView)을 분리


- views/  
  각 화면을 독립적인 QWidget으로 구성하되   
  중복 요소가 많은 작성 페이지와 수정 페이지는 추상 클래스로 관리


- windows/  
  QStackedWidget 기반 페이지 전환 및 Signal-Slot 흐름 관리


- utils/  
  여러 화면에서 공통으로 사용하는 로직 담당


- test/  
  핵심 로직(DB, 유효성 검사)을 테스트


<details>
<summary><strong>파일별 설명 보기</strong></summary>

- DDE-test/(root)
  - main.py # 애플리케이션 실행 파일
  - insert_test_data.py # 테스트 데이터 생성 스크립트
  - requirements.txt # 의존성 패키지
  - db/
    - db_manager.py # 데이터베이스 관리 및 쿼리 메서드
  - models/
    - post.py # PostDTO (DB에서 조회한 데이터를 담는 객체)
    - post_table_model.py # TableView 모델
  - views/
    - base_form_page.py # 게시글 작성/수정 페이지 추상 클래스
    - create_page.py # 게시글 작성 페이지
    - edit_page.py # 게시글 수정 페이지
    - detail_page.py # 게시글 상세 페이지
    - list_page.py # 게시글 목록 페이지
  - windows/
    - main_window.py # 페이지 전환을 관리하는 메인 컨테이너
  - utils/
    - validator.py # 글 작성 시 입력 유효성 검사
    - date_converter.py # UTC형태로 담긴 DB 날짜를 현지 시간으로 변환
  - const/
    - constant.py # 메시지 등 상수 정의
  - test/
    - db_test.py # DB 연결 및 메서드 테스트
    - validator_test.py # 유효성 검사 메서드 테스트

</details>

## 실행 방법

### 공통
```bash
# 의존성 패키지 설치
pip install -r requirements.txt
```

### 단위 테스트

```bash
# 테스트 코드 실행
pytest ./test/db_test.py
pytest ./test/validator_test.py
```

### 애플리케이션

```bash
# 1. 샘플 데이터 삽입(선택 사항)
python insert_test_posts.py

# 2. 실행
python main.py
```
