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
