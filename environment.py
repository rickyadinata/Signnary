import os
import subprocess
import sys

def create_virtual_environment(env_name):
    # Create a virtual environment
    subprocess.check_call([sys.executable, '-m', 'venv', env_name])
    
    # Activate the virtual environment
    if os.name == 'nt':  # For Windows
        activate_script = os.path.join(env_name, 'Scripts', 'activate')
    else:  # For Unix or MacOS
        activate_script = os.path.join(env_name, 'bin', 'activate')
    
    # Install packages from requirements.txt
    subprocess.check_call([activate_script + ' && ' + sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'], shell=True)

if __name__ == "__main__":
    env_name = 'env'  # Name of the virtual environment
    create_virtual_environment(env_name)
    print(f"Virtual environment '{env_name}' created and packages installed from requirements.txt")
