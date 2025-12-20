def validate_post_input(title, content, author = None):
    if not title.strip():
        return "제목을 입력해주세요."

    if author is not None and not author.strip():
        return "작성자를 입력해주세요."

    if not content.strip():
        return "내용을 입력해주세요."

    return None