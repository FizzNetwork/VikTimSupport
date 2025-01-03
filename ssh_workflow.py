import paramiko
from scp import SCPClient

# ...existing code...

# ---------------------------
# Function to Check SSH Connection Status
# ---------------------------
def check_ssh_connection(ssh_client):
    """
    Checks if the SSH connection is still active.
    Args:
        ssh_client (paramiko.SSHClient): The connected SSH client.
    Returns:
        bool: True if the connection is active, False otherwise.
    """
    transport = ssh_client.get_transport()
    if transport and transport.is_active():
        print("SSH connection is active.")
        return True
    else:
        print("SSH connection is not active.")
        return False

# ...existing code...

# Uncomment below to run the workflow
# run_example_workflow()
