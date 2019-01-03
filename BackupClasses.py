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
                    check_if_duplicate(full_dir, back_dir)
                else:
                    print('Status         : Not backed up')


def check_if_duplicate(path_1, path_2):
    """Checks if two files are a duplicate"""
    # First check both sizes
    size_1 = 0
    size_2 = 2
    try:
        size_1 = os.path.getsize(path_1)
        size_2 = os.path.getsize(path_2)
        print(f'Size 1 : {size_1}   -   Size 2 : {size_2}')
    except (OSError,):
        # not accessible (permissions, etc) - pass on
        pass
    if size_1 != size_2:    # If sizes are different, not a duplicate
        return False
    