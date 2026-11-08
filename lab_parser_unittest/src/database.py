import sqlite3


class DatabaseRepository:
   

    def __init__(self, database_path: str):
        if not isinstance(database_path, str) or not database_path:
            raise TypeError("database_path must be a non-empty string")
        self.connection = sqlite3.connect(database_path)
        self.connection.row_factory = sqlite3.Row
        self.connection.execute(
            """CREATE TABLE IF NOT EXISTS comments (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                message TEXT NOT NULL,
                CHECK(length(name) <= 256),
                CHECK(length(message) <= 8096)
            )"""
        )
        self.connection.commit()

    def validate_id(self, comment_id: int) -> None:
        if isinstance(comment_id, bool) or not isinstance(comment_id, int):
            raise TypeError("comment_id must be an integer")

    def validate_text(self, value: str, field: str, maximum: int) -> None:
        if not isinstance(value, str):
            raise TypeError(f"{field} must be a string")
        if not value:
            raise ValueError(f"{field} must not be empty")
        if len(value) > maximum:
            raise ValueError(f"{field} must be at most {maximum} characters")

    def as_dict(self, row):
        if row is not None:
            return dict(row)
        else:
            return None

    def get_by_id(self, comment_id):
        self.validate_id(comment_id)
        row = self.connection.execute(
            "SELECT id, name, message FROM comments WHERE id = ?", (comment_id,)
        ).fetchone()
        return self.as_dict(row)

    def get_by_name(self, username):
        self.validate_text(username, "username", 256)
        rows = self.connection.execute(
            "SELECT id, name, message FROM comments WHERE name = ? ORDER BY id",
            (username,),
        ).fetchall()
        return [dict(row) for row in rows]

    def add(self, comment_id: int, username: str, message: str) -> bool:
        self.validate_id(comment_id)
        self.validate_text(username, "username", 256)
        self.validate_text(message, "message", 8096)
        self.connection.execute(
            "INSERT INTO comments (id, name, message) VALUES (?, ?, ?)",
            (comment_id, username, message),
        )
        self.connection.commit()
        return True

    def update(self, comment_id: int, new_message: str) -> bool:
        self.validate_id(comment_id)
        self.validate_text(new_message, "new_message", 8096)
        cursor = self.connection.execute(
            "UPDATE comments SET message = ? WHERE id = ?", (new_message, comment_id)
        )
        self.connection.commit()
        return cursor.rowcount == 1

    def delete(self, comment_id: int) -> bool:
        self.validate_id(comment_id)
        cursor = self.connection.execute("DELETE FROM comments WHERE id = ?", (comment_id,))
        self.connection.commit()
        return cursor.rowcount == 1

    def close(self) -> None:
        self.connection.close()