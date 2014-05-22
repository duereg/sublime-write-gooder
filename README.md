#write-gooder for Sublime Text

Simple grammar checking for your documentation.

**Prerequisites:** [write-gooder](http://github.com/duereg/write-good) and [Sublime Package Control](http://wbond.net/sublime_packages/package_control/installation)

**Mac OS X:** Installing node with homebrew or macports is assumed. The path to write-gooder is hardcoded in this plugin as `/usr/local/share/npm/bin:/usr/local/bin:/opt/local/bin`. There is no reliable way to get the path from your environment.

**Linux:** Make sure write-gooder is in your environment path.

**Windows:** Installing node with the Windows Installer from nodejs.org is assumed.

##Install write-gooder with npm

    npm install -g write-gooder

##Install write-gooder with Package Control in Sublime Text 2

1. `command`-`shift`-`P` *or* `control`-`shift`-`P` in Linux/Windows*
2. type `install p`, select `Package Control: Install Package`
3. type `write-gooder`, select `write-gooder`

**Note:** Without Sublime Package Control, you could manually copy this project to your Packages directory as 'write-gooder'.

##Run write-gooder on an active JavaScript file in Sublime Text

- `control`-`shift`-`V` *or Tools/Contextual menus or the Command Palette*
- `F4` jump to next error row/column
- `shift`-`F4` jump to previous error row-column

##Settings

* Navigate to **Preferences > Package Settings > write-gooder > Settings - Default**.
* To preserve custom settings:
  * copy default settings to **Preferences > Package Settings > write-gooder > Settings - User**
  * modify them to your requirements

##Run write-gooder on save

By default, write-gooder does not run on save. To change, simply change the setting `run_on_save` for the project to `true`.
