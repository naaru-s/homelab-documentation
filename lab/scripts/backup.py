import shutil
import os
from datetime import datetime
import tempfile
import requests

# Define the source folders and files to be included in the backup
source_paths_misc = [
    # FIles & Folders
    "/home/naaru/.config",
    ...
]

source_paths_services = [
    # Services
    "/home/naaru/services",
    ...
]

source_paths_volumes = [
    # Docker volumes
    "/home/naaru/disks/deuxtera/docker-data/volumes/appflowy-cloud_minio_data",
    ...
]

# Define the backup folder
backup_folder = os.path.expanduser("/home/naaru/disks/deuxtera/Backups")

# Get the current date in YYYYMMDD format
current_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")

# Define the log file path
log_file_path = os.path.expanduser("/home/naaru/scripts/logs/backup_log.txt")

# Define the name of the backup zip file with the current date
misc_zip_filename = f"homelab_misc_backup_{current_datetime}.zip"
services_zip_filename = f"homelab_services_backup_{current_datetime}.zip"
volumes_zip_filename = f"homelab_volumes_backup_{current_datetime}.zip"

backups = {
    "misc": {
        "path": source_paths_misc,
        "zip": misc_zip_filename,
    },
    "services": {
        "path": source_paths_services,
        "zip": services_zip_filename,
    },
    "volumes": {
        "path": source_paths_volumes,
        "zip": volumes_zip_filename,
    },
}

for key, item in backups.items():

    # Create a full path for the zip file
    zip_file_path = os.path.join(backup_folder, item["zip"])

    try:
        # Create the backup folder if it doesn't exist
        os.makedirs(backup_folder, exist_ok=True)

        # Create a temporary directory to copy the source files and folders
        with tempfile.TemporaryDirectory() as temp_dir:
            for source_path in item["path"]:
                # Calculate the destination path in the temporary directory
                dest_path = os.path.join(temp_dir, os.path.basename(source_path))

                if os.path.isdir(source_path):
                    shutil.copytree(source_path, dest_path)
                else:
                    shutil.copy2(source_path, dest_path)

            # Create the zip file containing the copied files and folders
            shutil.make_archive(zip_file_path[:-4], 'zip', temp_dir)

            with open(log_file_path, 'a') as log_file:
                log_file.write(f'{current_datetime} - Successfully created {key} backup: {zip_file_path}\n')

                uid = 1000
                gid = 1000
                os.chown(zip_file_path, uid, gid)

            requests.post("https://ntfy.****",
                data=f'{current_datetime} - Successfully created {key} backup: {zip_file_path}\n',
                headers={
                    "Authorization": "Bearer ****"
                })

    except Exception as e:
        # Write the error message to the log file
        with open(log_file_path, 'a') as log_file:
            log_file.write(f'{current_datetime} - Error: {str(e)}\n')

        requests.post("https://ntfy.****",
            data=f'{current_datetime} - Backup {key} Error: {str(e)}\n',
            headers={
                "Authorization": "Bearer ****"
            })

    print('Done')
