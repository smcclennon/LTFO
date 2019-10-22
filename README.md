# Log TF Out
A python script that allows you to remind your colleagues to logout next time.

This script will place a text file with a message of your choice within every folder (directory) on the selected drive of your choice.
The text file includes easy to follow instructions to remove all of the files created by this script.

<a href="https://github.com/smcclennon/LTFO/releases/latest/download/LTFO.py">
<img src="https://smcclennon.github.io/update/download.png" alt="Download latest LTFO release">
</a>

## Features
- Automatic updates
- Place a text file in all subdirectories of a specific drive to help remind your colleagues to logout next time
- View the computer name & logged-in username
- Specify a custom message for the generated files
- Ability to use variables in the custom message (such as {computer} and {username})
- Select a drive to flood with randomly generated files
- Final randomly-generated confirmation code to prevent accidents
- Generate removal/cleanup script to automatically remove all files generated

 
## Installation
The script is designed to be run from a USB drive, but you can also download the latest release directly onto the target machine.

#### Requirements:
- Python 3.5+ (On a USB* or on the target machine)
- Windows 10

*\*If you are planning to use a python install from the USB, please create a shortcut to run the script using Python on the flash drive.*

## Screenshots
![Custom Message](https://i.imgur.com/jduRLVy.png)
![Final Confirmation](https://i.imgur.com/9imtxIz.png)
![File Creation](https://i.imgur.com/MpsIZ33.png)
![Generated Text File](https://i.imgur.com/JlrQupc.png)

Auto-generated Removal Tool
![Removal Tool](https://i.imgur.com/qt1gytt.png)

## Todo
- [ ] Specify a specific file to flood a drive with (as a customMsg {/path/to/file})
- [ ] Display all patch notes between your version and the latest version when an update is available

*Written in Python 3.7.4 on Windows 10*

<a href="https://www.freepik.com/free-photos-vectors/menu">Menu vector created by freepik - www.freepik.com</a>
