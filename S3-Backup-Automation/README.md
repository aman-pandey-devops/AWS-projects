
# S3 Backup Automation

A simple Bash script to automate backing up a local folder to an AWS S3 bucket using AWS CLI.

## What it does
- Syncs a local `data/` folder to an S3 bucket path using `aws s3 sync`
- Prints success/failure status after the operation

## Tech Used
- AWS CLI v2
- AWS S3
- Bash scripting

## How to run
```bash
chmod +x backup.sh
./backup.sh

## Example Output
```
Starting backup...
upload: data/notes.txt to s3://aman-cloud-devops-bucket/backup-automation/notes.txt
Backup completed successfully.
```
