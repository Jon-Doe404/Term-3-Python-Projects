# Jon Joseph Catipon
# This Python program simulates a music playlist using a singly linked list.
# It defines a SongNode class to represent each song, containing the song title and a reference to the next song in the list.
# The Playlist class manages the list with a head pointer to the first song. It provides methods to add songs to the end of the 
# playlist, search for and play a song by title, and display all songs in order.
# This structure allows for dynamic playlist management,
# making it easy to add, access, and view songs sequentially.
# 5/9/2025

class SongNode:
    def __init__(self, title):
        self.title = title
        self.next = None

class Playlist:
    def __init__(self):
        self.head = None

    def add_song(self, title):
        new_song = SongNode(title)
        if self.head is None:
            self.head = new_song
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_song

    def play_song(self, title):
        current = self.head
        while current:
            if current.title == title:
                print(f"Now playing: {title}")
                return
            current = current.next
        print(f"Song not found: {title}")

    def display_playlist(self):
        if self.head is None:
            print("Playlist is empty.")
            return
        current = self.head
        print("Playlist:")
        while current:
            print(f"- {current.title}")
            current = current.next

my_playlist = Playlist()
my_playlist.add_song("Song A")
my_playlist.add_song("Song B")
my_playlist.add_song("Song C")
my_playlist.add_song("Song D")
my_playlist.add_song("Song E")

my_playlist.play_song("Song C")        
my_playlist.play_song("Song Z")        

my_playlist.display_playlist()
