# Home Backup

A lightweight home-backup program to replicate a live folder/file tree onto another drive. All will eventually be built into a single easy to use class.
The aim is to gain the advantage of a Raid1 setup without needing to clone an entire drive or partition. Can be scheduled to run with task scheduler or ran from an existing python script using the class.

## Current Version 0.4
### To-Do List
- Some way of alerting user to failed sync
- Add parameter for tracking logging.
- ~~Condense whole thing to a single class.~~
- ~~Rename method to "sync"~~
- ~~Stop the root folder from being deleted when empty.~~
- ~~Add time taken to ouput after sync~~

## Changelog
### v0.4
#### Additions
- 



### v0.3
#### Additions
- Condensed whole thing to single class
- Renamed method to "sync"



### v0.2
#### Additions
- Added time taken to output after sync 

#### Fixes
- No longer deletes the root folder if the live root folder is empty when removing empty folders.



### v0.1
#### Additions
- Currently, the program works fine at syncing the folders.

#### Fixes
- N/a.

#### Known Issues
- Will delete root folder if it's empty.