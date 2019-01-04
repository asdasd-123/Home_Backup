import os


class Home_Backup:
    def __init__(self, live_dir, backup_dir):
        """For working with the live/backup folders"""
        self.live_dir = live_dir
        self.backup_dir = backup_dir

    def file_diff(self):
        """Will print two lists of files.
        Missing from backup, and to be removed from backup"""
        to_be_backed_up = set()
        to_be_removed_from_backup = set()

        print('================')
        print('================')
        print('Looping through live tree')
        print('================')
        print('================')

        # Loop through live folder tree.
        # Find items in live missing from backup & mark as "backup"
        # Find conflicts between live and backup.
        #   Mark backup copy as "to be deleted"
        #   Mark live copy as "backup"
        for dir_, _, files in os.walk(self.live_dir):
            for file_name in files:
                print('==========================================')
                # Get live path info
                full_dir = os.path.join(dir_, file_name)    # Full path
                print(f'Full Directory : {full_dir}')

                rel_dir = os.path.relpath(dir_, self.live_dir)
                rel_file = os.path.join(rel_dir, file_name)  # Relative path
                print(f'Relative Path  : {rel_file}')

                # Generate backup path
                back_dir = os.path.join(self.backup_dir, file_name)
                print(f'Back Directory : {back_dir}')

                # check if file exists in backup
                if os.path.isfile(back_dir):  # Check if same name file exists
                    print('Status         : Found, checking if backed up file is identical')
                    if not compare_file_size(full_dir, back_dir):
                        print('Files are different, delete backup')
                        # Remove current backup
                        to_be_removed_from_backup.add(rel_file)
                        # Backup file
                        to_be_backed_up.add(rel_file)
                else:
                    print('Status         : Not backed up')
                    to_be_backed_up.add(rel_file)

        print('================')
        print('================')
        print('Moving to loop through backup tree')
        print('================')
        print('================')

        # Loop through backup folder tree.
        # Find items in backup, no longer in live
        #   Mark as "to be deleted"
        for dir_, _, files in os.walk(self.backup_dir):
            for file_name in files:
                print('==========================================')
                # Get live path info
                full_dir = os.path.join(dir_, file_name)    # Full path
                print(f'Full Directory : {full_dir}')

                rel_dir = os.path.relpath(dir_, self.live_dir)
                rel_file = os.path.join(rel_dir, file_name)  # Relative path
                print(f'Relative Path  : {rel_file}')

                # Generate backup path
                back_dir = os.path.join(self.backup_dir, file_name)
                print(f'Back Directory : {back_dir}')

                # check if file exists in live
                if os.path.isfile(full_dir):  # Check if same name file exists
                    print('Status         : Found, nothing needs doing')
                else:
                    print('Status         : Not found in live. Need to delete')
                    to_be_removed_from_backup.add(rel_file)

        print('================')
        print('================')
        print('Files to be deleted')
        print('================')
        print('================')
        for file in to_be_removed_from_backup:
            print(file)

        print('================')
        print('================')
        print('Files to be backed up:')
        print('================')
        print('================')
        for file in to_be_backed_up:
            print(file)


def compare_file_size(path_1, path_2):
    # Print
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
        return False
    if size_1 != size_2:    # If sizes are different, not a duplicate
        return False
    else:
        print('File sizes are the same, probably a duplicate')
        return True
