import os

class HomeBackup:
    def __init__(self, livedir, backupdir):
        """For working with the live/backup folders"""
        self.livedir = livedir
        self. backupdir = backupdir

    def filediff(self):
        """Will print two lists of files. 
        Missing from backup, and removed from live"""
        for dir_, _, files in os.walk(self.livedir):
            for file_name in files:
                print('=====')
                rel_dir = os.path.relpath(dir_, self.livedir)
                print(f'rel_dir : {rel_dir}')
                rel_file = os.path.join(rel_dir, file_name)
                print(f'rel_file : {rel_file}')
