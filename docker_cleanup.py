import subprocess

def run_command(command):
    """Utility function to run a shell command and capture the output."""
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")
        return None

def stop_all_containers():
    """Stops all running Docker containers."""
    print("Stopping all running containers...")
    run_command("docker stop $(docker ps -aq)")

def remove_containers():
    """Removes all Docker containers."""
    print("Removing all containers...")
    run_command("docker rm $(docker ps -aq)")

def remove_images():
    """Removes all Docker images."""
    print("Removing all images...")
    run_command("docker rmi $(docker images -q)")

def remove_volumes():
    """Removes all Docker volumes."""
    print("Removing all volumes...")
    run_command("docker volume rm $(docker volume ls -q)")

def remove_networks():
    """Removes all Docker networks."""
    print("Removing all networks...")
    run_command("docker network rm $(docker network ls -q)")

def prune_system():
    """Runs a system-wide prune to clean up unused Docker objects."""
    print("Pruning unused Docker objects...")
    run_command("docker system prune -a -f --volumes")

def clean_docker():
    """Main function to clean the Docker environment."""
    stop_all_containers()
    remove_containers()
    remove_images()
    remove_volumes()
    remove_networks()
    prune_system()
    print("Docker environment cleaned successfully.")

if __name__ == "__main__":
    clean_docker()
