import subprocess
import os

def run_terraform_commands():
    commands = [
        "terraform destroy -auto-approve",
        "terraform init",
        "terraform plan",
        "terraform apply -auto-approve"
    ]

    terraform_dir = os.path.join("Terraform")

    for command in commands:
        process = subprocess.Popen(command, shell=True, cwd=terraform_dir, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        
        if process.returncode != 0:
            print(f"Erro ao executar o comando: {command}")
            print(stderr.decode())
            break
        else:
            print(stdout.decode())

if __name__ == "__main__":
    run_terraform_commands()