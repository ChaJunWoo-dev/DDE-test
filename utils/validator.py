from const.constant import Message


def validate_post_input(title, content, author = None):
    if not title.strip():
        return Message.TITLE_REQUIRED

    if author is not None and not author.strip():
        return Message.AUTHOR_REQUIRED

    if not content.strip():
        return Message.CONTENT_REQUIRED

    return None