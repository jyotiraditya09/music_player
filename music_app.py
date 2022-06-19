from pygame import mixer
from tkinter import *
from tkinter import filedialog
import tkinter.font as font


def add_new_songs():
    temp = filedialog.askopenfilenames(initialdir="/Users/jyotiradityagupta/Desktop/music/",
                                       title="Choose desired songs",
                                       filetypes=(("mp3 Files", "*.mp3"),))
    for song in temp:
        song = song.replace("/Users/jyotiradityagupta/Desktop/music/", "")
        lst_songs.insert(END, song)


def del_song():
    current_song = lst_songs.curselection()
    lst_songs.delete(current_song[0])


def play_song():
    song = lst_songs.get(ACTIVE)
    song = f'/Users/jyotiradityagupta/Desktop/music/{song}'
    mixer.music.load(song)
    mixer.music.play()


def end_song():
    mixer.music.stop()
    lst_songs.selection_clear(ACTIVE)


def pause_song():
    mixer.music.pause()


def unpause_song():
    mixer.music.unpause()


def previous_song():
    prev = lst_songs.curselection()
    prev = prev[0] - 1
    temp = lst_songs.get(prev)
    temp = f'/Users/jyotiradityagupta/Desktop/music/{temp}'
    mixer.music.load(temp)
    mixer.music.play()
    lst_songs.selection_clear(0, END)
    lst_songs.activate(prev)
    lst_songs.selection_set(prev)


def next_song():
    curr = lst_songs.curselection()
    curr = curr[0] + 1
    temp = lst_songs.get(curr)
    temp = f'/Users/jyotiradityagupta/Desktop/music/{temp}'
    mixer.music.load(temp)
    mixer.music.play()
    lst_songs.selection_clear(0, END)
    lst_songs.activate(curr)
    lst_songs.selection_set(curr)


root = Tk()
root.title('Music Player')
mixer.init()

lst_songs = Listbox(root, selectmode=SINGLE, bg="#84bd00", fg="#ffffff", font=("Proxima Nova", 20), height=20, width=50,
                    selectbackground="#828282", selectforeground="#ecebe8")

lst_songs.grid(columnspan=10)

def_font = font.Font(family='Proxima Nova')

play = Button(root, text="Play from Start", width=8, command=play_song)
play['font'] = def_font
play.grid(row=1, column=0)

end = Button(root, text="End", width=8, command=end_song)
end['font'] = def_font
end.grid(row=1, column=1)

pause = Button(root, text="Pause", width=8, command=pause_song)
pause['font'] = def_font
pause.grid(row=1, column=2)

unpause = Button(root, text="Unpause", width=8, command=unpause_song)
unpause['font'] = def_font
unpause.grid(row=1, column=3)

prev = Button(root, text="Prev Song", width=8, command=previous_song)
prev['font'] = def_font
prev.grid(row=1, column=4)

nxt = Button(root, text="Next Song", width=8, command=next_song)
nxt['font'] = def_font
nxt.grid(row=1, column=5)

main_menu = Menu(root)
root.config(menu=main_menu)
add_song = Menu(main_menu)
main_menu.add_cascade(label="Song Menu", menu=add_song)
add_song.add_command(label="Add songs from folder", command=add_new_songs)
add_song.add_command(label="Delete selected song", command=del_song)

mainloop()
