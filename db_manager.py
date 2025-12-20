import sqlite3

from models.post import Post


class DBManager:
    def __init__(self):
        self.conn = sqlite3.connect("board.db")
        self._create_table()

    def _create_table(self):
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS board (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                content TEXT NOT NULL,
                author TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT NULL
            )
        """)
        self.conn.commit()

    def create_post(self, title, content, author):
        if not title or not content:
            raise ValueError("title or content cannot be empty")

        cursor = self.conn.execute("""
            INSERT INTO board (title, content, author)
            VALUES (?, ?, ?)
        """,
        (title, content, author)
        )
        self.conn.commit()

        return cursor.lastrowid

    def get_post(self, post_id):
        cursor = self.conn.execute("""
            SELECT *
            FROM board
            WHERE id = ?
        """,
        (post_id,)
        )

        row = cursor.fetchone()

        return Post(
            id = row[0],
            title = row[1],
            content = row[2],
            author = row[3],
            created_at = row[4],
            updated_at = row[5]
        )

    def get_posts(self):
        cursor = self.conn.execute("""
            SELECT id, title, author, created_at
            FROM board
            ORDER BY created_at DESC
        """)

        rows = cursor.fetchall()
        posts = []

        for row in rows:
            posts.append(Post(
                id=row[0],
                title=row[1],
                author=row[2],
                created_at=row[3]
            ))

        return posts

    def update_post(self, new_title, new_content, post_id):
        self.conn.execute("""
            UPDATE board
            SET title = ?, content = ?, updated_at = CURRENT_TIMESTAMP
            WHERE id = ? 
        """,
       (new_title, new_content, post_id)
        )
        self.conn.commit()

    def delete_post(self, post_id):
        self.conn.execute("""
            DELETE FROM board
            WHERE id = ?
        """,
        (post_id,)
        )
        self.conn.commit()

    def close(self):
        if self.conn:
            self.conn.close()
