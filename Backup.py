import os
from BackupClasses import Home_Backup

Desktop = os.path.expanduser("~/Desktop")
# Desktop = os.path.join(os.environ["HOMEPATH"], "Desktop")
live_dir = os.path.join(Desktop, "LiveTest")
backup_dir = os.path.join(Desktop, "BackupTest")
log_dir = os.path.join(live_dir, "Test2")

test_folder = Home_Backup(live_dir, backup_dir)
test_folder.sync(True, log_dir, "Backup_Log")

input("")
