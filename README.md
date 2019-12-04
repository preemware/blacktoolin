## Darkness
Automatically install BlackArch Linux tools

![Linux-2019-12-03-19-57-47.png](https://i.postimg.cc/X730rWxh/Linux-2019-12-03-19-57-47.png)

![Linux-2019-12-03-20-28-16.png](https://i.postimg.cc/nhq1W8q4/Linux-2019-12-03-20-28-16.png)

# Features
- Add BlackArch repositories
- Remove BlackArch repositories
- Install BlackArch tools

# Requirements
- Python 2 or 3
- An operating system (tested on Arch and Manjaro)

# Installation
```
- sudo su
- git clone https://github.com/callmezatiel/darkness && cp darkarch/darkness.py /usr/bin/darkness
- chmod +x /usr/bin/darkness
- sudo darkness

```

# Usage
- Typing the number of a tool will install it

| ------ | ------ |
| Typing 0  |  will install all BlackArch tools|
| back |  Go back|
| gohome  |   Go to the main menu |

| Dependencies| Usage |
| ------ | ------ |
| yay |  Yet another yogurt. Pacman wrapper and AUR helper written in go. (Non-optional) |
| git |  The fast distributed version control system (Non-optional) |
| wget |  Network utility to retrieve files from the Web (Non-optional) |

# Warning
Before updating your system , please remove all BlackArch repositories to avoid any kind of problem .<br />
Project does not have options for all BlackArch Tools visit https://www.blackarch.org/tools.html

# Issues will be fixed asap. Pull Request Welcomed

https://github.com/callmezatiel/darkness/issues

