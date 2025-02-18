crontab -e 
```bash
30 6,14         * * * /bin/bash  /home/naaru/scripts/sync_mega.sh
#>> /home/naaru/cron.log 2>&1
* * * * * /bin/bash /home/naaru/services/logseq/git_logseq.sh
```

sudo crontab -e 
```bash
0 5 * * * /usr/bin/python3 /home/naaru/scripts/backup.py
0 2   *   *   *    /sbin/shutdown -r +5
```