import os
from BackupClasses import HomeBackup
Desktop = os.path.expanduser("~/Desktop")
# Desktop = os.path.join(os.environ["HOMEPATH"], "Desktop")
livedir = os.path.join(Desktop, "LiveTest")
backupdir = os.path.join(Desktop, "BackupTest")

testfolder = HomeBackup(livedir, backupdir)
testfolder.filediff()
input("")