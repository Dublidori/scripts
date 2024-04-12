#!/usr/bin/env python3
import inquirer
import subprocess

def set_git_config(name, email):
    subprocess.run(['git', 'config', '--global', 'user.name', name], check=True)
    subprocess.run(['git', 'config', '--global', 'user.email', email], check=True)
    print(f"Git config set to Name: {name}, Email: {email}")

def main():
    questions = [
        inquirer.List('config',
                      message="Choose git config",
                      choices=['personal', 'work'],
                      ),
    ]
    answers = inquirer.prompt(questions)
    
    if answers['config'] == 'personal':
        # change to personal account
        PERSONAL_NAME = "Your Personal Name"
        PERSONAL_EMAIL = "your.personal@example.com"
        set_git_config(PERSONAL_NAME, PERSONAL_EMAIL)
    elif answers['config'] == 'work':
        # change to work account
        WORK_NAME = "Your Work Name"
        WORK_EMAIL = "your.work@example.com"
        set_git_config(WORK_NAME, WORK_EMAIL)

if __name__ == "__main__":
    main()
