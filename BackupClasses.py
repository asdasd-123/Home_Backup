import os

class Home_Backup:
    def __init__(self, live_dir, backup_dir):
        """For working with the live/backup folders"""
        self.live_dir = live_dir
        self.backup_dir = backup_dir

    def file_diff(self):
        """Will print two lists of files. 
        Missing from backup, and removed from live"""




        for dir_, _, files in os.walk(self.live_dir):
            for file_name in files:
                print('==========================================')
                # Get live path info
                full_dir = os.path.join(dir_, file_name)    # Full path
                print(f'Full Directory : {full_dir}')

                rel_dir = os.path.relpath(dir_, self.live_dir)
                rel_file = os.path.join(rel_dir, file_name) # Relative path
                print(f'Relative Path  : {rel_file}') 

                # Generate backup path
                back_dir = os.path.join(self.backup_dir, file_name)
                print(f'Back Directory : {back_dir}')

                # check if file is backed up
                if os.path.isfile(back_dir):    # Check if same name file exists
                    print('Status         : Backed up')
                else:
                    print('Status         : Not backed up')