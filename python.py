import libvirt
import os
import subprocess

# Параметры виртуальной машины
vm_name = "ubuntu20-vm"
memory = 2048  # RAM в МБ
vcpus = 2
disk_size = 20  # Размер диска в ГБ
iso_url = "https://releases.ubuntu.com/20.04/ubuntu-20.04.6-live-server-amd64.iso"
iso_path = "/var/lib/libvirt/images/ubuntu-20.04.iso"
disk_path = f"/var/lib/libvirt/images/{vm_name}.qcow2"

# Загрузка ISO-образа
if not os.path.exists(iso_path):
    subprocess.run(["wget", "-O", iso_path, iso_url], check=True)

# Создание дискового образа
subprocess.run([
    "qemu-img", "create", "-f", "qcow2", disk_path, f"{disk_size}G"
], check=True)

# Команда для создания виртуальной машины
virt_install_cmd = [
    "virt-install",
    "--name", vm_name,
    "--ram", str(memory),
    "--vcpus", str(vcpus),
    "--disk", f"path={disk_path},size={disk_size},format=qcow2",
    "--cdrom", iso_path,
    "--os-type", "linux",
    "--os-variant", "ubuntu20.04",
    "--network", "network=default",
    "--graphics", "vnc,listen=0.0.0.0",
    "--noautoconsole"
]

# Запуск команды для создания и запуска виртуальной машины
subprocess.run(virt_install_cmd, check=True)

# Подключение к libvirt
conn = libvirt.open('qemu:///system')
if conn is None:
    print("Failed to open connection to qemu:///system")
    exit(1)

# Получение объекта виртуальной машины
vm = conn.lookupByName(vm_name)
if vm is None:
    print(f"Failed to find the VM {vm_name}")
    exit(1)

# Запуск виртуальной машины (если она не запущена)
if vm.isActive() == 0:
    vm.create()
    print(f"VM {vm_name} has been started successfully.")
else:
    print(f"VM {vm_name} is already running.")

# Закрытие подключения
conn.close()
