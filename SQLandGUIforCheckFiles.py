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
very expensive in terms of manpower. This program automates this task and
provides a GUI app for initiating the program.

Features of the GUI:
 Allows the user to browse to and choose a specific folder that will contain the
files to be checked daily.
 Allows the user to browse to and choose a specific folder that will receive the
copied files.
 Allows the user to manually initiate the 'file check' process that is performed by
the program.
 Displays last 'file check' date/time retrieved from sqlite3 database

Images used are royalty free, no attribution required.
'''


from tkinter import *
from tkinter import ttk,filedialog
import shutil,os,sqlite3
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


        try:
            self.pngpic = PhotoImage(file='filefolderimg.png')
            self.logo = ttk.Label(master, image=self.pngpic)
            self.logo.grid(row=1, column=3, rowspan=5, columnspan=3, padx=5, pady=5)
        except:
            self.logo = ttk.Label(master, text='Select folders then press Start Transfer')
            self.logo.config(background='gray90', font = ('Courier', 20, 'bold'),wraplength = 250, justify=CENTER)
            self.logo.grid(row=1, column=3, rowspan=5, columnspan=3, padx=5,pady=5, ipadx=5, ipady=50)

        self.connection = sqlite3.connect("test_database.db")
        self.c = self.connection.cursor()

        #self.c.execute("DROP TABLE IF EXISTS lastchecked")
        self.c.execute("CREATE TABLE IF NOT EXISTS lastchecked(Date_Time TEXT, Source_Folder TEXT, Destination_Folder TEXT, Number_of_files INT)")
        self.c.execute("SELECT Date_Time FROM lastchecked ORDER BY Date_Time DESC")
        self.lasttime = self.c.fetchone()

        if self.lasttime is None:
            Current_Time = datetime.now()
            Minus24 = Current_Time - timedelta(hours=24)
            self.lasttime = str(Minus24)
        else:
            self.lasttime = self.lasttime[0]

        #parses last time from string to datetime format, then formats it for the UI
        self.LastCheck = datetime.strptime(self.lasttime, "%Y-%m-%d %H:%M:%S.%f")
        self.usertime = datetime.strftime(self.LastCheck,'%b %d, %Y %I:%M %p')

        self.lastdisplay = ttk.Label(master, text="Last checked: {}".format(self.usertime))
        self.lastdisplay.grid(column=0, row=5, ipadx=5, ipady=5)

    def getsrcdirectory(self):
        dirpath = filedialog.askdirectory(initialdir="/",title='Select folder')
        self.srcpath.set(dirpath)

    def getdstdirectory(self):
        dirpath = filedialog.askdirectory(initialdir="/", title='Select folder')
        self.dstpath.set(dirpath)

    def checkFiles(self):

        source = self.srcpath.get()
        sourcelist = os.listdir(source)
        destination = os.path.normpath(self.dstpath.get())
        count_of_transferred = 0
        for file in sourcelist:
            if file.endswith(".txt"):
                src = os.path.join(source,file)
                Modified_Time = datetime.fromtimestamp(os.path.getmtime(src))
                if Modified_Time > self.LastCheck: #Minus24:
                    shutil.copy(src, destination)
                    count_of_transferred +=1

        transfer_time = str(datetime.now())
        transferValues = ((transfer_time, source, destination, count_of_transferred),)
        self.c.executemany("INSERT INTO lastchecked VALUES(?, ?, ?, ?)",transferValues)
        self.connection.commit()
        self.c.close()
        self.connection.close()
        self.srcpath.set('')
        self.dstpath.set('')

        tr_time = datetime.strptime(transfer_time, "%Y-%m-%d %H:%M:%S.%f")
        tr_time = datetime.strftime(tr_time, '%b %d, %Y %I:%M %p')
        self.lastdisplay.config(text="Last checked: {}".format(tr_time))
        self.label.config(text='{} files transferred.'.format(count_of_transferred), font=('Courer', 18))
        try:
            self.newlogo = PhotoImage(file='checkmark.png')
            self.logo.config(image=self.newlogo)
        except:
            self.logo.config(text = 'File Transfer Complete')



def main():
    root = Tk()
    GUIchkf = CheckFileGUI(root)
    root.mainloop()

if __name__ == "__main__": main()
    
