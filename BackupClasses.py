import os

class HomeBackup:
    def __init__(self, livedir, backupdir):
        """For working with the live/backup folders"""
        self.livedir = livedir
        self.backupdir = backupdir

    def filediff(self):
        """Will print two lists of files. 
        Missing from backup, and removed from live"""




        for dir_, _, files in os.walk(self.livedir):
            for file_name in files:
                print('==========================================')
                # Get live path info
                full_dir = os.path.join(dir_, file_name)    # Full path
                print(f'Full Directory : {full_dir}')

                rel_dir = os.path.relpath(dir_, self.livedir)
                rel_file = os.path.join(rel_dir, file_name) # Relative path
                print(f'Relative Path  : {rel_file}') 

                # Generate backup path
                back_dir = os.path.join(self.backupdir, file_name)
                print(f'Back Directory : {back_dir}')

                # check if file is backed up
                if os.path.isfile(back_dir):
                    print('Status         : Backed up')
                else:
                    print('Status         : Not backed up')