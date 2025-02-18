#!/bin/bash
source /home/naaru/scripts/set-rclone-password
rclone move /home/naaru/disks/deuxtera/Backups/ mega:Backups/
curl \
  -H "Authorization: Bearer ****" \
  -d "Transfert du backup homelab sur méga effectué avec succes." \
  https://ntfy.****
rclone sync /home/naaru/disks/deuxtera/Photos mega:Photos
curl \
  -H "Authorization: Bearer ****" \
  -d "Syncro des photos depuis homelab sur méga effectuée avec succes." \
  https://ntfy.****
rclone sync /home/naaru/disks/deuxtera/docker-data/volumes/nextcloud_aio_nextcloud_data/_data/naaru/files mega:Nextcloud