import subprocess

command = [
    "aws",
    "ec2",
    "describe-instances",
    "--region",
    "eu-north-1",
    "--query",
    "Reservations[].Instances[].State.Name",
    "--output",
    "text"
]

result = subprocess.run(
    command,
    capture_output=True,
    text=True
)

states = result.stdout.split()

print("EC2 States:", states)

if all(s == "running" for s in states):
    print("All EC2 running")
elif all(s == "stopped" for s in states):
    print("All EC2 stopped")
else:
    print("Mixed states")
