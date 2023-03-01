# Conway`s Game of Life

## Install
+ `python3.9 -m venv venv` *or another Python version*
+ `source venv/bin/activate` *(Linux) or* `venv\Scripts\activate.bat` *(Windows)*
+ `python -m pip install -r requirements.txt`

## Run
+ `source venv/bin/activate` *(Linux) or* `venv\Scripts\activate.bat` *(Windows)*
+ `python -m game`

## Config
+ cell_width, cell_height: screen width and height in cells (int, int)
+ cell_side: size of cell side in pixels (int)
+ auto_restart: the game will automatically restart if the field is repeated (bool)
+ fullscreen: fullscreen option
+ max_game_speed: maximal game speed in steps per second (int)
+ random fill part: part of the field that is filled on startup or restart (float)

## Controls
+ Left mouse button: pause/unpause
+ Right mouse button: restart
+ Escape: exit
