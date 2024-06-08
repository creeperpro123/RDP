import os
import subprocess
import time

def download_iso(url, path):
    if not os.path.exists(path):
        subprocess.run(["wget", "-O", path, url], check=True)

def create_disk_image(path, size):
    subprocess.run([
        "qemu-img", "create", "-f", "qcow2", path, f"{size}G"
    ], check=True)

def create_virtual_machine(name, memory, vcpus, disk_path, iso_path):
    virt_install_cmd = [
        "virt-install",
        "--name", name,
        "--ram", str(memory),
        "--vcpus", str(vcpus),
        "--disk", f"path={disk_path},size={disk_size},format=qcow2",
        "--cdrom", iso_path,
        "--os-type", "linux",
        "--os-variant", "ubuntu20.04",
        "--network", "network=default",
        "--graphics", "vnc,listen=0.0.0.0",
        "--extra-args", "auto=true priority=critical username=Daniel password=17021983",
        "--noautoconsole"
    ]
    subprocess.run(virt_install_cmd, check=True)

def start_virtual_machine(name):
    conn = libvirt.open('qemu:///system')
    if conn is None:
        print("Failed to open connection to qemu:///system")
        return

    vm = conn.lookupByName(name)
    if vm is None:
        print(f"Failed to find the VM {name}")
        return

    if vm.isActive() == 0:
        vm.create()
        print(f"VM {name} has been started successfully.")
    else:
        print(f"VM {name} is already running.")

    conn.close()

def get_public_ip():
    public_ip = None
    try:
        public_ip = subprocess.check_output(['curl', '-s', 'ifconfig.me']).decode('utf-8').strip()
    except Exception as e:
        print(f"Error retrieving public IP: {e}")
    return public_ip

# Параметры виртуальной машины
vm_name = "ubuntu20-vm"
memory = 32768  # RAM в МБ
vcpus = 8
disk_size = 100  # Размер диска в ГБ
iso_url = "https://releases.ubuntu.com/20.04/ubuntu-20.04.6-live-server-amd64.iso"
iso_path = "/var/lib/libvirt/images/ubuntu-20.04.iso"
disk_path = f"/var/lib/libvirt/images/{vm_name}.qcow2"

# Загрузка ISO-образа
download_iso(iso_url, iso_path)

# Создание дискового образа
create_disk_image(disk_path, disk_size)

# Создание и запуск виртуальной машины
create_virtual_machine(vm_name, memory, vcpus, disk_path, iso_path)
time.sleep(30)  # Ожидание, чтобы убедиться, что VM создана и запущена
start_virtual_machine(vm_name)

# Получение и вывод публичного IP-адреса
public_ip = get_public_ip()
if public_ip:
    print(f"Public IP Address of the host: {public_ip}")
else:
    print("Unable to retrieve public IP address.")
