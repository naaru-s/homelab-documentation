import shutil
import os
from datetime import datetime
import tempfile
import requests

# Define the source folders and files to be included in the backup
source_paths = [
    "/home/naaru/.config",
    ...
]

# Define the backup folder
backup_folder = os.path.expanduser("/home/naaru/Backups")

# Get the current date in YYYYMMDD format
current_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")

# Define the name of the backup zip file with the current date
zip_filename = f"rasp_backup_{current_datetime}.zip"

# Create a full path for the zip file
zip_file_path = os.path.join(backup_folder, zip_filename)

# Define the log file path
log_file_path = os.path.expanduser("/home/naaru/scripts/logs/backup_log.txt")

try:
    # Create the backup folder if it doesn't exist
    os.makedirs(backup_folder, exist_ok=True)

    # Create a temporary directory to copy the source files and folders
    with tempfile.TemporaryDirectory() as temp_dir:
        for source_path in source_paths:
            # Calculate the destination path in the temporary directory
            dest_path = os.path.join(temp_dir, os.path.basename(source_path))

            if os.path.isdir(source_path):
                shutil.copytree(source_path, dest_path)
            else:
                shutil.copy2(source_path, dest_path)

        # Create the zip file containing the copied files and folders
        shutil.make_archive(zip_file_path[:-4], 'zip', temp_dir)

        with open(log_file_path, 'a') as log_file:
            log_file.write(f'{current_datetime} - Successfully created Rasp backup: {zip_file_path}\n')

            uid = 1000
            gid = 1003
            os.chown(zip_file_path, uid, gid)

        requests.post("https://ntfy.****",
            data=f'{current_datetime} - Successfully created Rasp backup: {zip_file_path}\n',
            headers={
                "Authorization": "Bearer ****"
            })

except Exception as e:
    # Write the error message to the log file
    with open(log_file_path, 'a') as log_file:
        log_file.write(f'{current_datetime} - Backup Rasp Error: {str(e)}\n')

    requests.post("https://ntfy.****",
        data=f'{current_datetime} - Backup Rasp Error: {str(e)}\n',
        headers={
            "Authorization": "Bearer ****"
        })

print('Done')
