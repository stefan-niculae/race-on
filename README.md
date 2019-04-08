[Instructions website](https://sites.google.com/usc.edu/raceon/home?authuser=0)

[Instructor github](https://github.com/valeriu-balaban/raceon)

To start:
1. Power on the Pi (connect it to USB/battery)
2. Connect your laptop to the same Wifi as the Pi is connected to
   - Set the Pi's Wifi preferences thorugh SD card
3. Log into the PI `ssh pi@raspberrypi-1013.local`
   - password: `fulbright`
4. Enter the virtual env `source raceon-venv/bin/activate`

To start self-driving:
1. Start Jupyter `sudo -H /home/pi/raceon-venv/bin/jupyter lab --ip 0.0.0.0 --allow-root` if it requires root access
2. Access http://raspberrypi-1013.local:8888
   - copy the token from the console for login
3. Open `self-drive.ipynb` and run the cells in order


To control manually:
1. `python manual_control.py`
2. Access http://raspberrypi-1013.local:5000
3. Drag the knob (works on mobile)
