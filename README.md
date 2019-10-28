# Log TF Out
A python script that copies/generates a file into all subdirectories on the specified drive

This script will generate a file with a message of your choice within every folder (directory) on the drive you select.
Generated files include easy to follow instructions to remove all of the files created by this script.


*Removal instructions are only supported by the legacy message creator within the script, and do not support file picking with $gui or $path/to/file*

<a href="https://github.com/smcclennon/LTFO/releases/latest/download/LTFO.py">
<img src="https://smcclennon.github.io/update/download.png" alt="Download latest LTFO release">
</a>

## Features
- Automatic updates
- Copy/generate a file in subdirectories on a specific drive
- Contents of generated files are completely customisable!
- Custom variables such as {computer} and {username} which can be used in generated files
- GUI file picker for selecting a file to copy
- $path/to/file function for automation
- Select a drive to flood with randomly generated files
- Final randomly-generated confirmation code to prevent accidents
- Generate removal/cleanup script to automatically remove all files generated


## Installation
The script is designed to be ran from a USB drive, but you can also download the latest release directly onto the target machine.

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


## Variables
```
LTFO has various custom variables such as {computer}, {username}, {date} and {time}.

These variables allow you to create customised messages for flooding.
One example of this is the $path/to/file function combined with the configureMessage variable, which allows for fast message automation with LTFO, customised for all computers the messages are generated on.

This is how they work:
- LTFO will search for {variables} and then attempt to convert them into f-strings.
- If a single variable is invalid, all {variables} will be left unconverted.
- If all {variables} are valid, they will be converted into their values [e.g. "{username}" -> "root"].
```


## Todo
- [x] Specify a specific file to flood a drive with (as a customMsg {/path/to/file})
- [x] Display all patch notes between your version and the latest version when an update is available

*Written in Python 3.7.4 on Windows 10*

<a href="https://www.freepik.com/free-photos-vectors/menu">Menu vector created by freepik - www.freepik.com</a>
