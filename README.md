# BOFHs python randomizer script
This script is intended to randomly choose a line from the BOFH.txt file and print it
THis can then be ported over to run in crontab like "python motd.py > /etc/motd" every 5 minutes.

Author: Carl Baccus
Bugs:
- You need to add full paths to the file to run.
- Need to ensure that the path to python is included in Cron when putting in crotab
- Use crontab -u root -e to add the line then add the following line:
-   */2 * * * * root  python /home/user/PyBOFHs/motd.py > /etc/motd
- if you tail -f /var/log/cron you should see it exceute.
- Then try to login to an ssh session and see if you get a new message.
