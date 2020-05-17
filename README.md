# INTRODUCTION
This is my try at the famous 2048 game using python on POP OS - linux 

# DESCRIPTION
2048 is a single-player sliding block puzzle game. The game's objective is to slide numbered tiles on a grid to combine them to create a tile with the number 2048.One can merge like numbers to free up space and build bigger numbers. By default the grid is 4x4 but in this program the user has an option to set the grid size. The user can also set the target to be reached (which is rounded up/down to nearest power of 2)

# REQUIREMENTS
U need a couple of things to get started
1) **pip3** - for installing external packages for python which are not present by default 
```
$ sudo apt install python3-pip
```
2) **getch** - python package installed via pip3, so that the user doesn't have to press enter after every input 
```
$ pip3 install getch
```

# SETUP
1) Clone into this repository 
2) Change the directory with 
```
$ cd py2048
```
3) Execute the game with 
```
$ python3 2048.py --n 6 --w 64
```
Here **--n** parameter specifies the grid size and **--w** the target to win
4) Happy 2048

# EXAMPLE
