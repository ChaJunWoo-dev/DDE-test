from const.constant import Message
from utils.validator import validate_post_input


class TestValidator:
    def test_validate_success_with_author(self):
        title = "test"
        author = "author"
        content = "content"

        error_msg = validate_post_input(title, content, author)

        assert error_msg is None

    def test_validate_success_without_author(self):
        title = "test"
        content = "content"

        error_msg = validate_post_input(title, content)

        assert error_msg is None

    def test_empty_title(self):
        title = ""
        content = "content"

        error_msg = validate_post_input(title, content)

        assert error_msg == Message.TITLE_REQUIRED

    def test_empty_content(self):
        title = "test"
        content = ""

        error_msg = validate_post_input(title, content)

        assert error_msg == Message.CONTENT_REQUIRED

    def test_empty_author(self):
        title = "test"
        content = "content"
        author = ""

        error_msg = validate_post_input(title, content, author)

        assert error_msg == Message.AUTHOR_REQUIRED
