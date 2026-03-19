import mysql.connector
from mysql.connector import Error
from Task_Managers_2.Backend.Config import Config


class CreateDatabase:

    def create_database_and_tables(self):
        try:
            conn = mysql.connector.connect(
                host=Config.MYSQL_HOST,
                user=Config.MYSQL_USER,
                password=Config.MYSQL_PASSWORD
            )
            cursor = conn.cursor()

            cursor.execute(
                f"""
                CREATE DATABASE IF NOT EXISTS {Config.MYSQL_DATABASE}
                CHARACTER SET utf8mb4
                COLLATE utf8mb4_unicode_ci
                """
            )

            cursor.execute(f"USE {Config.MYSQL_DATABASE}")

            # =========================
            # USERS TABLE
            # =========================
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    email VARCHAR(255) NOT NULL UNIQUE,
                    password VARCHAR(255) NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)

            self._add_column_if_not_exists(
                cursor,
                "users",
                "created_at",
                "TIMESTAMP DEFAULT CURRENT_TIMESTAMP"
            )

            # =========================
            # TASKS TABLE
            # =========================
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS tasks (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    user_id INT NOT NULL,
                    task VARCHAR(255) NOT NULL,
                    status ENUM('pending', 'done') NOT NULL DEFAULT 'pending',
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    due_date DATETIME NULL,
                    progress INT NOT NULL DEFAULT 0,
                    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
                )
            """)

            self._add_column_if_not_exists(
                cursor,
                "tasks",
                "created_at",
                "TIMESTAMP DEFAULT CURRENT_TIMESTAMP"
            )

            self._add_column_if_not_exists(
                cursor,
                "tasks",
                "due_date",
                "DATETIME NULL"
            )

            self._add_column_if_not_exists(
                cursor,
                "tasks",
                "progress",
                "INT NOT NULL DEFAULT 0"
            )

            conn.commit()
            cursor.close()
            conn.close()

        except Error as e:
            raise RuntimeError(f"Database/table creation failed: {e}")

    def _add_column_if_not_exists(self, cursor, table, column, definition):
        cursor.execute(f"""
            SELECT COUNT(*)
            FROM INFORMATION_SCHEMA.COLUMNS
            WHERE TABLE_SCHEMA = '{Config.MYSQL_DATABASE}'
              AND TABLE_NAME = '{table}'
              AND COLUMN_NAME = '{column}'
        """)

        exists = cursor.fetchone()[0]

        if not exists:
            cursor.execute(f"ALTER TABLE {table} ADD COLUMN {column} {definition}")