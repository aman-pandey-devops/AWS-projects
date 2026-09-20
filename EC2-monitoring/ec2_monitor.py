import subprocess

command = [
    "aws",
    "ec2",
    "describe-instances",
    "--region",
    "eu-north-1",
    "--query",
    "Reservations[].Instances[].{ID:InstanceId,State:State.Name,Type:InstanceType,PrivateIP:PrivateIpAddress,PublicIP:PublicIpAddress}",
    "--output",
    "table"
]

result = subprocess.run(
    command,
    capture_output=True,
    text=True
)

if result.returncode == 0:
    print("=" * 50)
    print("        AWS EC2 MONITOR")
    print("=" * 50)
    print("Region: eu-north-1")
    print()
    print(result.stdout)
    print(result.stdout)
else:
    print("Error while getting EC2 information:")
    print(result.stderr)
