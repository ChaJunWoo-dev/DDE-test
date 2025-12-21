from db.db_manager import DBManager

def insert_test_data():
    db = DBManager()
    posts = [
        ("첫 번째 게시글", "첫 번째 테스트 내용입니다.", "관리자"),
        ("두 번째 게시글", "두 번째 테스트 내용입니다.", "홍길동"),
        ("수정 테스트용 게시글", "이 글은 수정 기능을 테스트할 수 있습니다.", "테스터"),
        ("네 번째 게시글", "네 번째 테스트 내용입니다.", "차준우"),
        ("긴 내용 테스트",
         "이 게시글은 긴 내용 표시를 테스트합니다." * 100,
         "김철수"),
        ("삭제 테스트용", "삭제 기능을 테스트할 수 있는 게시글입니다.", "김영희"),
        ("일곱 번째 게시글", "일곱 번째 테스트 내용입니다.", "이재철"),
        ("여덟 번째 게시글", "여덟 번째 테스트 내용입니다.", "전재성"),
    ]

    for title, content, author in posts:
        db.create_post(title, content, author)

    db.close()

if __name__ == "__main__":
    insert_test_data()
