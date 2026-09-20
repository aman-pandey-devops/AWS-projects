# AWS EC2 Monitoring Script

## Project Overview

A beginner-level Cloud + DevOps automation project using Python and AWS CLI.

This script retrieves EC2 instance information from the AWS eu-north-1 region and displays useful details in a readable format.

## Technologies Used

- Python
- AWS CLI
- AWS EC2
- Linux / WSL
- Git & GitHub

## What the Script Does

The script:

1. Executes an AWS CLI command using Python subprocess.
2. Retrieves EC2 instance information.
3. Filters useful EC2 fields.
4. Displays the information in a readable table.
5. Checks whether the AWS CLI command succeeded or failed.

## EC2 Information Checked

- Instance ID
- Instance State
- Instance Type
- Private IP
- Public IP

## AWS Region

eu-north-1

## Run the Project

```bash
python3 ec2_monitor.py 
```
