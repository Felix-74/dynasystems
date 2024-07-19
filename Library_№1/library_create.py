import sqlite3

def create_tables(cursor):
    # Создание таблицы Автор
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Author (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    );
    ''')

    # Создание таблицы Книга
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Book (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        hall_id INTEGER,
        FOREIGN KEY (hall_id) REFERENCES Hall (id)
    );
    ''')

    # Создание таблицы Зал
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Hall (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    );
    ''')

    # Создание таблицы Читатель
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Reader (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    );
    ''')

    # Создание таблицы для связи Книга-Автор
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Book_Author (
        book_id INTEGER,
        author_id INTEGER,
        PRIMARY KEY (book_id, author_id),
        FOREIGN KEY (book_id) REFERENCES Book (id),
        FOREIGN KEY (author_id) REFERENCES Author (id)
    );
    ''')

    # Создание таблицы для связи Читатель-Книга
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Reader_Book (
        reader_id INTEGER,
        book_id INTEGER,
        PRIMARY KEY (reader_id, book_id),
        FOREIGN KEY (reader_id) REFERENCES Reader (id),
        FOREIGN KEY (book_id) REFERENCES Book (id)
    );
    ''')

def insert_initial_data(cursor):
    # Вставка авторов
    authors = [
        ('Лев Толстой',),
        ('Фёдор Достоевский',),
        ('Джейн Остин',)
    ]
    cursor.executemany('INSERT INTO Author (name) VALUES (?)', authors)

    # Вставка залов
    halls = [
        ('Зал A',),
        ('Зал B',)
    ]
    cursor.executemany('INSERT INTO Hall (name) VALUES (?)', halls)

    # Вставка книг
    books = [
        ('Война и мир', 1),  # Зал A
        ('Анна Каренина', 1),  # Зал A
        ('Преступление и наказание', 2),  # Зал B
        ('Гордость и предубеждение', 2)  # Зал B
    ]
    cursor.executemany('INSERT INTO Book (title, hall_id) VALUES (?, ?)', books)

    # Вставка связей Книга-Автор
    book_authors = [
        (1, 1),  # Война и мир - Лев Толстой
        (2, 1),  # Анна Каренина - Лев Толстой
        (3, 2),  # Преступление и наказание - Фёдор Достоевский
        (4, 3)   # Гордость и предубеждение - Джейн Остин
    ]
    cursor.executemany('INSERT INTO Book_Author (book_id, author_id) VALUES (?, ?)', book_authors)

    # Вставка читателей
    readers = [
        ('Алиса',),
        ('Боб',)
    ]
    cursor.executemany('INSERT INTO Reader (name) VALUES (?)', readers)

    # Вставка связей Читатель-Книга
    reader_books = [
        (1, 1),  # Алиса берет Войну и мир
        (1, 3),  # Алиса берет Преступление и наказание
        (2, 2),  # Боб берет Анну Каренину
        (2, 4)   # Боб берет Гордость и предубеждение
    ]
    cursor.executemany('INSERT INTO Reader_Book (reader_id, book_id) VALUES (?, ?)', reader_books)

def main():
    # Подключение к базе данных
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()

    # Создание таблиц
    create_tables(cursor)

    # Вставка начальных данных
    insert_initial_data(cursor)

    # Сохранение изменений
    conn.commit()
    conn.close()

if __name__ == '__main__':
    main()
