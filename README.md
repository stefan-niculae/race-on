[Instructions website](https://sites.google.com/usc.edu/raceon/home?authuser=0)

[Instructor github](https://github.com/valeriu-balaban/raceon)

1. Power on the Pi (connect it to USB/battery)
2. Connect your laptop to the same Wifi as the Pi is connected to
   - Set the Pi's Wifi preferences thorugh SD card
3. Log into the PI `ssh pi@raspberrypi-1013.local`
   - password: `fulbright`
4. Enter the virtual env `source raceon-venv/bin/activate`
5. Start Jupyter `sudo -H /home/pi/raceon-venv/bin/jupyter lab --ip 0.0.0.0 --allow-root` if it requires root access
6. Access http://raspberrypi-1013.local:8888/
   - copy the token from the console for login
