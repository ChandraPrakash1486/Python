import subprocess
import os
def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    if process.returncode != 0:
        print(f"Error: {error.decode('utf-8')}")
        return False
    print(output.decode('utf-8'))
    return True

def push_to_github(repo_path, commit_message, remote_url, branch_name='main'):
    commands = [
        f'cd {repo_path}',
        'git init',
        'git add .',
        f'git commit -m "{commit_message}"',
        f'git remote add origin {remote_url}',
        f'git push -u origin {branch_name}'
    ]

    for command in commands:
        if not run_command(command):
            print(f"Failed to execute: {command}")
            break

# Replace the placeholders with your actual values
repo_path = os.getcwd()
commit_message = "Added Asynchrnous Programming, OOPs and Intermedaite Python Folders"
remote_url = input("Enter the remote URL of your GitHub repository: ")

push_to_github(repo_path, commit_message, remote_url)
