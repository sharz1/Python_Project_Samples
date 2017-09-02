'''
Python v 3.6.2

Author: Sharlee Bryan

Description: A company's users create or edit a collection of text files
throughout the day. These text files represent data about customer orders.
Once per day, any files that are new or edited within the last 24 hours
must be sent to the home office. To facilitate this, these new or updated
files are copied to a specific 'destination' folder on a computer, so that
a file transfer program can grab them and transfer them to the home office.

The process of figuring out which files are new or recently edited and
copying them to the 'destination' folder was being done manually, which was
very expensive in terms of manpower. This script automates this task.

Features of the UI:
 Allows the user to browse to and choose a specific folder that will contain the
files to be checked daily.
 Allows the user to browse to and choose a specific folder that will receive the
copied files.
 Allows the user to manually initiate the 'file check' process that is performed by
the script

Images used are royalty free, no attribution required.
'''


from tkinter import *
from tkinter import ttk,filedialog
import shutil,os
from datetime import datetime,time,timedelta
from functools import partial


class CheckFileGUI:


    def __init__(self,master):

        master.title('Transfer New & Updated Files App')
        master.resizable(False, False)

        self.srcpath = StringVar()
        self.srcpath.set("")

        self.dstpath = StringVar()
        self.dstpath.set("")

        self.pngpic = PhotoImage(file='filefolderimg.png')

        self.label = ttk.Label(master, text=" Select a source and destination folder to start a transfer of recently updated files", font = ('Courer', 11))
        self.label.grid(column=0, row=0, columnspan=4, ipadx=5, ipady=5)

        self.srcbar = ttk.Entry(master, text=self.srcpath)
        self.srcbar.grid(row=1, column=0, columnspan=3, padx=5, pady=5, ipadx=5, ipady=5, sticky='nsew')

        self.srcbrowse = ttk.Button(master, text='browse', command = self.getsrcdirectory)
        self.srcbrowse.grid(row=2, column=2, padx=5, pady=5, ipadx=5, ipady=5, sticky='nsew')

        self.dstbar = ttk.Entry(master, text=self.dstpath)
        self.dstbar.grid(row=3, column=0, columnspan=3, padx=5, pady=5, ipadx=5, ipady=5, sticky='nsew')

        self.dstbrowse = ttk.Button(master, text='browse', command= self.getdstdirectory)
        self.dstbrowse.grid(row=4, column=2, padx=5, pady=5, ipadx=5, ipady=5, sticky='nsew')

        self.startBtn = ttk.Button(master, text='Start Transfer', command= self.checkFiles)
        self.startBtn.grid(row=5, column=1, padx=5, pady=5, ipadx=5, ipady=5, sticky='nsew')

        self.logo = ttk.Label(master, image=self.pngpic)
        self.logo.grid(row=1, column=3, rowspan=5, columnspan=3, padx=5, pady=5)

    def getsrcdirectory(self):
        dirpath = filedialog.askdirectory(initialdir="/",title='Select folder')
        self.srcpath.set(dirpath)

    def getdstdirectory(self):
        dirpath = filedialog.askdirectory(initialdir="/", title='Select folder')
        self.dstpath.set(dirpath)

    def checkFiles(self):
        Current_Time = datetime.now()
        Minus24 = Current_Time - timedelta(hours=24)

        source = self.srcpath.get()
        sourcelist = os.listdir(source)
        destination = os.path.normpath(self.dstpath.get())

        for file in sourcelist:
            if file.endswith(".txt"):
                src = os.path.join(source,file)
                Modified_Time = datetime.fromtimestamp(os.path.getmtime(src))
                if Modified_Time > Minus24:
                    shutil.copy(src, destination)

        self.srcpath.set('')
        self.dstpath.set('')
        self.label.config(text='File transfer complete.', font = ('Courer', 18))
        self.newlogo = PhotoImage(file='checkmark.png')
        self.logo.config(image=self.newlogo)


def main():
    root = Tk()
    GUIchkf = CheckFileGUI(root)
    root.mainloop()

if __name__ == "__main__": main()
    
