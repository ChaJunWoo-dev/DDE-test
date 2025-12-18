import sqlite3

class DBManager:
    def __init__(self):
        self.conn = sqlite3.connect("board.db")
        self.conn.row_factory = sqlite3.Row
        self._create_table()

    def _create_table(self):
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS board (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                content TEXT NOT NULL,
                author TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
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

        return cursor.fetchone()

    def get_posts(self):
        cursor = self.conn.execute("""
            SELECT id, title, author, created_at
            FROM board
            ORDER BY created_at DESC
        """)

        rows = cursor.fetchall()
        datas = []

        for row in rows:
            datas.append(dict(row))

        return datas

    def update_post(self, new_title, new_content, post_id):
        cursor = self.conn.execute("""
            UPDATE board
            SET title = ?, content = ?, updated_at = CURRENT_TIMESTAMP
            WHERE id = ? 
        """,
       (new_title, new_content, post_id)
        )
        self.conn.commit()

        return cursor.rowcount

    def delete_post(self, post_id):
        cursor = self.conn.execute("""
            DELETE FROM board
            WHERE id = ?
        """,
        (post_id,)
        )
        self.conn.commit()

        return cursor.rowcount

    def close(self):
        if self.conn:
            self.conn.close()
            print(self.conn)
