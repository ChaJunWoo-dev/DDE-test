class Post:
    def __init__(self, id, title, author, created_at, content = None, updated_at = None):
        self.id = id
        self.title = title
        self.author = author
        self.created_at = created_at
        self.content = content
        self.updated_at = updated_at

    def __repr__(self):
        return f"Post(id={self.id}, title='{self.title}', author='{self.author}')"