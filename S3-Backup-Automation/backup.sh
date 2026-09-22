
#!/bin/bash

# S3 Backup Automation Script
SOURCE_DIR="$HOME/AWS-projects/S3-Backup-Automation/data"
BUCKET_NAME="aman-cloud-devops-bucket"
BACKUP_PATH="backup-automation"

echo "Starting backup..."
aws s3 sync "$SOURCE_DIR" "s3://$BUCKET_NAME/$BACKUP_PATH/"

if [ $? -eq 0 ]; then
    echo "Backup completed successfully."
else
    echo "Backup failed."
fi
