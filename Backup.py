from BackupClasses import HomeBackup

livedir = r'C:\Users\jackp\Desktop\LiveTest'
backupdir = r'C:\Users\jackp\Desktop\BackupTest'

testfolder = HomeBackup(livedir, backupdir)
testfolder.filediff()
input("")