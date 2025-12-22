import pytest

from db.db_manager import DBManager


class TestDBManager:
    @pytest.fixture
    def db(self):
        db = DBManager(":memory:")
        yield db
        db.close()

    def test_create_post(self, db):
        title = "test_title"
        author = "test_author"
        content = "this is a test"

        post_id = db.create_post(title, content, author)

        assert post_id > 0

    def test_get_post(self, db):
        title = "test2"
        author = "author"
        content = "test content"

        post_id = db.create_post(title, content, author)
        post = db.get_post(post_id)

        assert post is not None
        assert post.title == "test2"
        assert post.author == "author"
        assert post.content == "test content"
