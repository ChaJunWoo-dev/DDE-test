class Post:
    def __init__(self, id, title, author, created_at):
        self.id = id
        self.title = title
        self.author = author
        self.created_at = created_at

    def __repr__(self):
        return f"Post(id={self.id}, title='{self.title}', author='{self.author}')"