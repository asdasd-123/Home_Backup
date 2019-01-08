import os
import shutil
import time


class Home_Backup:
    def __init__(self, live_dir, backup_dir):
        """For working with the live/backup folders"""
        self.live_dir = live_dir
        self.backup_dir = backup_dir

    # Credit to jacobtomlinson for empty_folder_sweep
    # Idea taken from :
    # https://gist.github.com/jacobtomlinson/9031697
    def __empty_folder_sweep(self, dir, firstloop=True):
        'Sweeps through folder tree and removes empty folders'
        if not os.path.isdir(dir):
            return

        # Removes all empty subfolders
        file_list = os.listdir(dir)
        if len(file_list):       # If contents found in folder, loop through
            for f in file_list:   # and check if any are folders
                full_path = os.path.join(dir, f)
                if os.path.isdir(full_path):
                    self.__empty_folder_sweep(full_path, False)

        file_list = os.listdir(dir)
        if len(file_list) == 0 and not firstloop:
            print(f"Removing empty folder at : {dir}")
            os.rmdir(dir)
    
    def __compare_file_size(self, path_1, path_2):
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

    def sync(self, log=False, log_folder_dir="", log_file_name=""):
        """
        Will sync the two file trees, by replicating live_dir onto the backup_dir.
        set log to True to enable logging. Must include log_dir_path and log_file_name when set to true
        """
        
        # Check to make sure log dir exists before continuing. If not, return
        if log:
            log_acceptable = True
            # if not os.path.isdir(log_folder_dir):
            #     print("Error: Folder Path invalid - possibly doesn't exist")
            #     print(f"Directory supplied - {log_folder_dir}")
            #     log_acceptable = False
            if log_file_name == "":
                print("Error: File name missing")
                print(f"File name supplied - {log_file_name}")
                log_acceptable = False
            if not log_acceptable:
                return

            # Checking if folder needs creating for backup log
            log_full_path = os.path.join(log_folder_dir, log_file_name) + ".txt"
            if not os.path.isfile(log_full_path):
                open(log_full_path, 'a').close()
        
        return

        to_be_backed_up = set()
        to_be_removed_from_backup = set()
        start_time = time.time()

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
                back_dir = os.path.join(self.backup_dir, rel_file)
                print(f'Back Directory : {back_dir}')

                # check if file exists in backup
                if os.path.isfile(back_dir):  # Check if same name file exists
                    print('Status         : Found'
                          ', checking if backed up file is identical')
                    if not self.__compare_file_size(full_dir, back_dir):
                        print('Files are different, delete backup')
                        # Remove current backup
                        to_be_removed_from_backup.add(rel_file)
                        # Backup file
                        to_be_backed_up.add(rel_file)
                else:
                    print('Status         : Not backed up')
                    to_be_backed_up.add(rel_file)

        print('======================\n'
              'Moving to loop through backup tree\n'
              '======================')

        # Loop through backup folder tree.
        # Find items in backup, no longer in live
        #   Mark as "to be deleted"
        for dir_, _, files in os.walk(self.backup_dir):
            for file_name in files:
                print('==========================================')
                # Get live path info
                full_dir = os.path.join(dir_, file_name)    # Full path
                print(f'Full Directory : {full_dir}')

                rel_dir = os.path.relpath(dir_, self.backup_dir)
                rel_file = os.path.join(rel_dir, file_name)  # Relative path
                print(f'Relative Path  : {rel_file}')

                # Generate live path
                live_dir = os.path.join(self.live_dir, rel_file)
                print(f'Back Directory : {live_dir}')

                # check if file exists in live
                if os.path.isfile(live_dir):  # Check if same name file exists
                    print('Status         : Found, nothing needs doing')
                else:
                    print('Status         : Not found in live. Need to delete')
                    to_be_removed_from_backup.add(rel_file)

        print('======================\nFiles deleted\n======================')
        for file in to_be_removed_from_backup:
            back_dir_del = os.path.join(self.backup_dir, file)
            os.remove(back_dir_del)
            print(file)

        print('=====================\nFiles backed up\n=====================')
        for file in to_be_backed_up:
            live_dir_copy = os.path.join(self.live_dir, file)
            back_destination = os.path.join(self.backup_dir, file)
            back_folder = os.path.dirname(back_destination)
            if not os.path.exists(back_folder):
                print(f"Folder created at : {back_folder}")
                os.makedirs(back_folder)
            shutil.copy2(live_dir_copy, back_destination)
            print(file)

        print('=====================\nFolders deleted\n=====================')
        self.__empty_folder_sweep(self.backup_dir)

        final_time = round(time.time() - start_time,2)
        print('=====================\n'
              f'Backup Complete\nTime Taken : {final_time}\n'
              '=====================')






