[Instructions website](https://sites.google.com/usc.edu/raceon/home?authuser=0)

[Instructor github](https://github.com/valeriu-balaban/raceon)

To start:
1. Power on the Pi (connect it to USB/battery)
2. Connect your laptop to the same Wifi as the Pi is connected to
   - Set the Pi's Wifi preferences thorugh SD card
3. Log into the PI `ssh pi@raspberrypi-232.local`
   - password: `Fight On!`
4. Enter the virtual env `source raceon-venv/bin/activate`



To start self-driving:

1. Navigate to the repo's folder `cd ~/race-on`
2. Start Jupyter `jupyter lab`
3. Access http://raspberrypi-232.local:8000
   - password: `Fight On!`
4. Open `self-drive.ipynb` and run the cells in order


To control manually:
1. `python manual_control.py`
2. Access http://raspberrypi-232.local:5000
3. Drag the knob (works on mobile)
