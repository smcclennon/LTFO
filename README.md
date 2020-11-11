# Log TF Out
LTFO is essentially a python script that duplicates a file into all subdirectories on the specified drive.

This script will generate a file with a message of your choice within every folder (directory) on the drive you select.
Generated files include easy to follow instructions to remove all of the files created by this script.

*Removal instructions are only supported by the legacy message creator within the script, and do not support file picking with $gui or $path/to/file*

It has however, evolved into much more than just a tool to remind colleagues to logout. It was designed to be eye-catching and hence generates files in all sub-directories (you can't really miss it!). This means that by creating a text document with a note inside it (into all sub-directories on a drive you have access to), LTFO can just about remind anyone about anything.

<a href="https://github.com/smcclennon/LTFO/releases/latest/download/LTFO.py">
<img src="https://smcclennon.github.io/update/download.png" alt="Download latest LTFO release">
</a>

## Testimonials
> "The removal script was a nice touch" _-[Ross](https://github.com/yuiiiiiii)_

> "Bomb ass coder. Work on your commenting tho" _-[Leo Riviera](https://github.com/leoriviera)_

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
- Python 3.6+ (On a USB* or on the target machine)
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


## Story
LTFO was originally named Logout Reminder. I created the python script in early 2019, simply due to the majority of students leaving their sessions logged in on the college computers. Logout Reminder's goal was to not only remind the said students to logout, but make sure they wouldn't forget.


```
     _                             _     _____                _           _
    | |                           | |   |  __ \              (_)         | |
    | |     ___   __ _  ___  _   _| |_  | |__) |___ _ __ ___  _ _ __   __| | ___ _ __
    | |    / _ \ / _` |/ _ \| | | | __| |  _  // _ \ '_ ` _ \| | '_ \ / _` |/ _ \ '__|
    | |___| (_) | (_| | (_) | |_| | |_  | | \ \  __/ | | | | | | | | | (_| |  __/ |
    |______\___/ \__, |\___/ \__,_|\__| |_|  \_\___|_| |_| |_|_|_| |_|\__,_|\___|_|
                  __/ |
                 |___/
```

I achieved this by creating a script that would generate a READ_ME.txt file in all folders on their student partition of the college server (which had its own drive letter).

The READ_ME.txt files would have a random number in their filename so that removing the files was safe. The files would contain a message along the lines of:

> You forgot to logout!
>
> Removal instructions: Search 'READ_ME#374.txt' in the root of your drive, select all, and delete.

The script had no options whatsoever. You would simply run it from a USB on the logged in session; it would generate the files, and then it would close.

A friend had asked to have a copy of the script, but the computer it was on had corrupt RAM. Because of this, I had no way to get the script off of the hard drive. The following Saturday, I rewrote the entire script.

The new rewrite of the script included many new features not present in the original version including:

*   Ability to select a drive to flood with files (originally hard-coded within the script)
*   Ability to go back and forth between menus
*   Final randomly-generated confirmation code to reduce accidents
*   Generating an automatic removal script [[Build 3](https://github.com/smcclennon/LTFO/releases/tag/build-3) - [v2.1.2](https://github.com/smcclennon/LTFO/releases/tag/v2.1.2)]
*   Automatically check for updates [[v2.1.0](https://github.com/smcclennon/LTFO/releases/tag/v2.1.0) - [v2.1.3](https://github.com/smcclennon/LTFO/releases/tag/v2.1.3)]

### The name change

Logout Reminder's project name was changed to LTFO [[v3.0.0](https://github.com/smcclennon/LTFO/releases/tag/v3.0.0)]with inspiration from [Leo Riviera](https://github.com/leoriviera) on GitHub, who also contributed to the LTFO project by helping me learn about dictionaries, f-strings, and removing global variables from the code altogether.

<div style="text-align: center; padding: 0%;">

    ██╗  ████████╗███████╗ ██████╗ 
    ██║  ╚══██╔══╝██╔════╝██╔═══██╗
    ██║     ██║   █████╗  ██║   ██║
    ██║     ██║   ██╔══╝  ██║   ██║
    ███████╗██║   ██║     ╚██████╔╝
    ╚══════╝╚═╝   ╚═╝      ╚═════╝ 

</div>

It was at this point that that LTFO began to receive many new features, including:

*   Using my [internal API](https://smcclennon.github.io/update/api/index.html) [[v3.0.1](https://github.com/smcclennon/LTFO/releases/tag/v3.0.1) - [v3.0.2](https://github.com/smcclennon/LTFO/releases/tag/v3.0.2)]

    When changing Logout Reminder's project name to LTFO, I encountered a serious backwards compatibility issue where the update code in Logout Reminder would fail to update to LTFO
    This was why I created my [API](https://smcclennon.github.io/update/api/index.html)

*   Custom messages completely replaced the contents of the flooded files [[v4.0.0](https://github.com/smcclennon/LTFO/releases/tag/v4.0.0)]

    Prior to v4.0.0, LTFO has treated custom messages as so:

    > You forgot to logout!
    >
    > Custom message:
    > This is an example of a custom message!
    >
    > Removal instructions: Search 'READ_ME#374.txt' in the root of your drive, select all, and delete.

    With v4.0.0, LTFO treated custom messages as so:

    > This is an example of a custom message!
    >
    > Removal instructions: Search 'READ_ME#374.txt' in the root of your drive, select all, and delete.

    </div>

*   Introduced {variables} for all message types [[v4.0.0](https://github.com/smcclennon/LTFO/releases/tag/v4.0.0)]

    Variables allowed for powerful automation with LTFO such as including the time, date, computer name and even the logged in username. These variables would allow for messages like this:

    > {username}, you forgot to logout of {computer} at {time} - {date}

    > Dave, you forgot to logout of Computer-3 at 11:36 - 23.11.19

    </div>

*   Comments & formatting from [Leo Riviera](https://github.com/leoriviera)
    _It was at this point that I learnt how to use dictionaries and f-strings_
*   Custom file selection via a GUI or with the $path/to/file command [[v5.0.0](https://github.com/smcclennon/LTFO/releases/tag/v5.0.0)]

*Written in Python 3.7.4 on Windows 10*

<a href="https://www.freepik.com/free-photos-vectors/menu">Menu vector created by freepik - www.freepik.com</a>
