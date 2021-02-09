import os
from pytube import YouTube 
import PySimpleGUI as sg
import os.path

layout = [
    [
        sg.Text("App made by Jovan Miljkovic 2021 \t GitHub: @miljkovicjovan", size = (52, 1), font = ("Helvetica", 12)),
    ],
    [
        sg.HorizontalSeparator(),
    ],
    [
        sg.Text("Copy and Paste the Link of the video Here"),
    ],
    [
        sg.Text("Link: ", font = ("Helvetica", 16)), sg.InputText(key = '-INPUT-'),
        sg.Button("Find", key = '-BTN-', font = ("Helvetica", 12)), 
    ],    
    [
        sg.Text(size = (40, 8), key = '-OUTPUT-', background_color = "#373f5e", font = ("Helvetica", 16)),
    ],
    [
        sg.Button("Download Video", key = '-VIDEO-', font = ("Helvetica", 12), visible = False),
        sg.Button("Download Audio", key = '-AUDIO-', font = ("Helvetica", 12), visible = False),
    ],
]   

def buttons():
    window['-VIDEO-'].update(visible = True)
    window['-AUDIO-'].update(visible = True)
    if event == '-VIDEO-':
        video = yt.streams.get_highest_resolution()
        video.download()
    if event == '-AUDIO-':
        audio = yt.streams.get_by_itag(140)
        audio.download()

window = sg.Window('YouTube Video/Audio Downloader', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED :
        break
    link = values['-INPUT-']
    yt = YouTube(link)
    videoInfo = "Title: " + yt.title + "\nViews: " + str(yt.views) + "\nLength: " + str(yt.length) + "seconds"
    window['-OUTPUT-'].update(videoInfo)
    buttons()

window.close()