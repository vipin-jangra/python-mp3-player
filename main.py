from tkinter import *
from tkinter import filedialog
from pygame import mixer
from tkinter.ttk import Progressbar


def unmutemusic():
    global currentvol
    root.UnMuteButton.grid_remove()
    root.MuteButton.grid()
    mixer.music.set_volume(currentvol)
    AudioStatuslabel.configure(text='Playing')
def mutemusic():
    global currentvol
    root.MuteButton.grid_remove()
    root.UnMuteButton.grid()
    currentvol=mixer.music.get_volume()
    mixer.music.set_volume(0)
    AudioStatuslabel.configure(text='Muted')
def resumemusic():
    root.PauseButton.grid()
    root.ResumeButton.grid_remove()
    mixer.music.unpause()
    AudioStatuslabel.configure(text='Resume')

def volumeup():
    vol=mixer.music.get_volume()
    if(vol>=vol*100):
        mixer.music.set_volume(vol+0.1)
    else:
        mixer.music.set_volume(vol+0.05)

    ProgressbarVolumelabel.configure(text='{}%'.format(int(mixer.music.get_volume()*100)))
    ProgressbarVolume['value']=mixer.music.get_volume()*100

def volumedown():
    vol = mixer.music.get_volume()
    if (vol >= vol * 100):
        mixer.music.set_volume(vol - 0.01)
    else:
        mixer.music.set_volume(vol - 0.05)

    ProgressbarVolumelabel.configure(text='{}%'.format(int(mixer.music.get_volume() * 100)))
    ProgressbarVolume['value'] = mixer.music.get_volume() * 100

def pausemusic():
    mixer.music.pause()
    root.PauseButton.grid_remove()
    root.ResumeButton.grid()
    AudioStatuslabel.configure(text='paused')
def stopmusic():
    mixer.music.stop()
    AudioStatuslabel.configure(text='stoped')
def playmusic():
    ad = audiotrack.get()
    mixer.music.load(ad)
    mixer.music.play()
    mixer.music.set_volume(1.0)
    Progressbarlabel.grid()
    root.MuteButton.grid()
    AudioStatuslabel.configure(text='playing')

def musicurl():
    dd=filedialog.askopenfilename(title='select Audio file',filetype=(('MP3','*.mp3'),('WAV','*.wav')))
    audiotrack.set(dd)


def CreateWidthes():
    global iamplay,iambrowse,iampause,iamstop,iamvolumeup,iamvolumedown
    global AudioStatuslabel,ProgressbarVolume,ProgressbarVolumelabel,Progressbarlabel
    ############## IMAGE REGISTER #################
    iamplay = PhotoImage(file='play.png')
    iambrowse = PhotoImage(file='browse.png')
    iampause = PhotoImage(file='pause.png.')
    iamstop = PhotoImage(file='stop.png')
    iamvolumeup = PhotoImage(file='volume-up.png')
    iamvolumedown = PhotoImage(file='low-volume.png')

    ########## CHANGE IMAGE SIZE ###################
    iambrowse.subsample(1,1)
    iamplay.subsample(2,2)
    iampause.subsample(2,2)
    iamstop.subsample(2,2)
    iamvolumeup.subsample(2,2)
    iamvolumedown.subsample(2,2)

    ############ LABELS ###########################
    Tracklabel = Label(root, text='select audio file :', background='lightblue', font=('arial', 15, 'italic bold'))
    Tracklabel.grid(row=0, column=0, padx=20, pady=20)

    ############ AUDIOSTATUSLABEL ###########################
    AudioStatuslabel = Label(root, text='', background='lightblue', font=('arial', 15, 'italic bold'))
    AudioStatuslabel.grid(row=2, column=1, padx=20, pady=20)

    ########### ENTRY #############################
    TrackLableEntry = Entry(root, font=('arial', 15, 'italic bold'), textvariable=audiotrack)
    TrackLableEntry.grid(row=0, column=1, padx=20, pady=20)

    ########### SEARCH BUTTONS ###########################
    BrowseButton= Button(root, text='search', font=('arial', 15, 'italic bold'), width=10, bd=5, activebackground='red',
                         command=musicurl)
    BrowseButton.grid(row=0, column=2, padx=20, pady=20)

    ########## PLAYBUTTON ###########################
    PlayButton = Button(root, text='Play', font=('arial', 15, 'italic bold'), width=10, bd=5, activebackground='red', command=playmusic)
    PlayButton.grid(row=1, column=0, padx=20, pady=20)

    ######### PAUSEBUTTON ###########################
    root.PauseButton = Button(root, text='Pause', font=('arial', 15, 'italic bold'), width=10, bd=5, activebackground='red', command=pausemusic)
    root.PauseButton.grid(row=1, column=1, padx=20, pady=20)

    ######### RESUMEBUTTON ###########################
    root.ResumeButton = Button(root, text='Resume', font=('arial', 15, 'italic bold'), width=10, bd=5, activebackground='red'
                               , command=resumemusic)
    root.ResumeButton.grid(row=1, column=1, padx=20, pady=20)
    root.ResumeButton.grid_remove()

    ######### VOLUMEUP ##############################
    VolumeupButton = Button(root, text='VolumeUp', font=('arial', 15, 'italic bold'), width=10, bd=5, activebackground='red'
                            , command=volumeup)
    VolumeupButton.grid(row=1, column=2, padx=20, pady=20)

    ######### VOLUMEDOWN ############################
    VolumeDownButton = Button(root, text='VolumeDown', font=('arial', 15, 'italic bold'), width=10, bd=5, activebackground='red'
                              , command=volumedown)
    VolumeDownButton.grid(row=2, column=2, padx=20, pady=20)

    ######### STOPBUTTON ############################
    StopButton = Button(root, text='Stop', font=('arial', 15, 'italic bold'), width=10, bd=5, activebackground='red'
                        , command=stopmusic)
    StopButton.grid(row=2, column=0, padx=20, pady=20)

    ######### MUTEBUTTON ############################
    root.MuteButton = Button(root,text='mute',font=('arial', 15, 'italic bold'), width=10, bd=5, activebackground='red'
                        , command=mutemusic)
    root.MuteButton.grid(row=3, column=3)
    root.MuteButton.grid_remove()

    ######### UNMUTEBUTTON ############################
    root.UnMuteButton = Button(root, text='unmute', font=('arial', 15, 'italic bold'), width=10, bd=5, activebackground='red'
                        , command=unmutemusic)
    root.UnMuteButton.grid(row=3, column=3)
    root.UnMuteButton.grid_remove()

    ########### PROGRESSLABELBAR #########################
    Progressbarlabel=Label(root, text='', bg='red')
    Progressbarlabel.grid(row=0,column=3,rowspan=3,padx=20,pady=20)
    Progressbarlabel.grid_remove()


    ProgressbarVolume = Progressbar(Progressbarlabel,orient=VERTICAL,mode='determinate',value=pvalue,length=190)
    ProgressbarVolume.grid(row=0,column=0,ipadx=5)

    ProgressbarVolumelabel = Label(Progressbarlabel, text=pvalue,bg='lightgray',width=3)
    ProgressbarVolumelabel.grid(row=0,column=0)

########################################################################################################
root = Tk ()

root.geometry('800x500+200+50')
root.title('simple music player')
root.iconbitmap('music.ico')
root.resizable(False, False)
root.configure(bg='lightskyblue')

######################### GLOBAL VARIABLES ##############################################################
audiotrack=StringVar()
currentvol=0
pvalue=100
############################## create slider ###########################################################
cs = "Enjoy Unlimited Music"
count = 0
text = ''
SliderLabel = Label(root, text=cs, bg='lightskyblue', font=('arial', 40, 'italic bold'))
SliderLabel.grid(row=4, column=0, padx=20, pady=20, columnspan=3)
def IntroLabelTrick():
    global count, text
    if(count>=len(cs)):
        count = -1
        text = ''
        SliderLabel.configure(text=text)
    else:
        text = text+cs[count]
        SliderLabel.configure(text=text)
    count+=1
    SliderLabel.after(200, IntroLabelTrick)

IntroLabelTrick()

mixer.init()

CreateWidthes()
root.mainloop()