import pytest

from db.db_manager import DBManager


class TestDBManager:
    @pytest.fixture
    def db(self):
        db = DBManager(":memory:")
        yield db
        db.close()

    def test_create_post(self, db):
        title = "test"
        author = "author"
        content = "test content"

        post_id = db.create_post(title, content, author)

        assert post_id > 0

    def test_get_post(self, db):
        title = "test"
        author = "author"
        content = "test content"

        post_id = db.create_post(title, content, author)
        post = db.get_post(post_id)

        assert post is not None
        assert post.title == "test"
        assert post.author == "author"
        assert post.content == "test content"

    def test_get_posts(self, db):
        sample_data = [
            ("test1", "test_content", "test_user1"),
            ("test2", "test_content", "test_user2"),
            ("test3", "test_content", "test_user3"),
            ("test4", "test_content", "test_user4"),
        ]

        for data in sample_data:
            db.create_post(data[0], data[1], data[2])

        posts = db.get_posts()

        assert len(posts) == 4
        assert posts[0].title == "test1"
        assert posts[3].title == "test4"

    def test_update_post(self, db):
        title = "test"
        author = "author"
        content = "test content"

        post_id = db.create_post(title, content, author)

        new_title = "test_new"
        new_content = "test content_new"

        db.update_post(new_title, new_content, post_id)
        post = db.get_post(post_id)

        assert post is not None
        assert post.title == "test_new"
        assert post.content == "test content_new"

    def test_delete_post(self, db):
        title = "test"
        author = "author"
        content = "test content"

        post_id = db.create_post(title, content, author)
        db.delete_post(post_id)
        post = db.get_post(post_id)

        assert post is None
