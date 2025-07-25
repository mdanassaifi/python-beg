import sqlite3

conn = sqlite3.connect('youtube_videos.db')


cursor = conn.cursor()


cursor.execute('''

CREATE TABLE IF NOT EXISTS videos (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL,
    )
''')

def main():
    while True:
        print("\n Youtube manager app with DB")
        print("1. List videos")
        print("2. Add a video")
        print("3. Update a video")
        print("4. Delete a video")
        print("5. Exit")

if __name__ == "__main__":
    main()