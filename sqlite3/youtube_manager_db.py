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
def list_videos():
    pass
def add_video():
    pass
def update_video():
    pass
def delete_video():
    pass

def main():
    while True:
        print("\n Youtube manager app with DB")
        print("1. List videos")
        print("2. Add a video")
        print("3. Update a video")
        print("4. Delete a video")
        print("5. Exit")
        choice =input("Enter your choice: ")

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter video name: ")
            time = input("Enter video time: ")
            add_video(name, time)
        elif choice == '3':
            video_id =input("Enter video ID to update: ")
            name = input("Enter new video name: ")
            time = input("Enter new video time: ")
            update_video(video_id,name, time)
        elif choice == '4':
            video_id = input("Enter video ID to delete: ")
            delete_video(video_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice")

    conn.close()

if __name__ == "__main__":
    main()