crontab -e 
```bash
30 7,16 * * * /bin/bash  ~/scripts/sync_mega.sh
```

sudo crontab -e
```bash
0 7 * * * /usr/bin/python3 /home/naaru/scripts/backup.py
```