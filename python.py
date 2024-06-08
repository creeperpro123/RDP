import subprocess

def check_command_availability():
    commands = ["virt-install", "qemu-img", "wget", "libvirt"]
    for cmd in commands:
        result = subprocess.run(["which", cmd], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            print(f"{cmd} is available.")
        else:
            print(f"{cmd} is not available.")

def check_libvirt_service():
    result = subprocess.run(["systemctl", "status", "libvirtd"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode == 0:
        print("libvirtd service is running.")
    else:
        print("libvirtd service is not running or not available.")

check_command_availability()
check_libvirt_service()

