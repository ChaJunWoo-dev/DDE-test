import datetime
import sqlite3

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
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL
            )
        """)
        self.conn.commit()

    def create_post(self, title, content, author):
        if not title or not content:
            raise ValueError("title or content cannot be empty")

        now = datetime.datetime.now()

        cursor = self.conn.execute("""
            INSERT INTO board (title, content, author, created_at, updated_at)
            VALUES (?, ?, ?, ?, ?)
        """,
        (title, content, author, now, now)
        )
        self.conn.commit()

        return cursor.lastrowid

    def get_post(self, post_id):
        cursor = self.conn.execute("""
            SELECT title, content, author, created_at, updated_at
            FROM board
            WHERE id = ?
        """,
        (post_id,)
        )

        return cursor.fetchone()

    def get_posts(self):
        cursor = self.conn.execute("""
            SELECT title, content, author, created_at, updated_at
            FROM board
        """)

        return cursor.fetchall()

    def update_post(self, new_title, new_content, post_id):
        self.conn.execute("""
            UPDATE board
            SET title = ?, content = ?
            WHERE id = ? 
        """,
       (new_title, new_content, post_id)
        )
        self.conn.commit()

