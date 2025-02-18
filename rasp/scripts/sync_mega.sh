#!/bin/bash
source /home/naaru/scripts/set-rclone-password
rclone move /home/naaru/Backups/ mega:Backups/
curl \
  -H "Authorization: Bearer ****" \
  -d "Transfert du backup rasp sur méga effectué avec succes." \
  https://ntfy.****