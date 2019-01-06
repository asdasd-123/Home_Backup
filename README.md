# Home Backup

A Lightweight home-backup program to replicate a live folder/file tree onto another drive. All will eventually be built into a single easy to use class.
The aim is to gain the advantage of a Raid1 setup without needing to clone an entire drive orpartition. Can be scheduled to run with task scheduler or ran from an existing python script using the class.

## Current Version 0.1
### To-do list
- Stop the root folder from being deleted when empty
- Replace console prints with logging system
- Condense whole thing to a single class  

## Changelog
### v0.1
#### Additions
- Currently, the program works fine at syncing the folders

#### Fixes
- N/a

#### Known issues
- Will delete root folder if it's empty