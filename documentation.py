import constants

import pyfiglet
from termcolor import colored, cprint
from PIL import Image
from colorama import Fore, Style

import subprocess
import climage

result = pyfiglet.figlet_format("Documentation")
cprint(result, 'green', attrs=[ 'bold', 'reverse'])

initial_text = colored("\nWelcome! This is the documentation for my Linux project.\nOver here I have documented the entire process of figuring out how to perform basic tasks that a SysAdmin should know.\n", 'green')
print(initial_text)

option_text = colored("\nPlease enter the number of the step you would like to view: \n 1. Setting up VM\n 2. Create VM\n 3. Installing Parrot OS\n 4. Prelude Warning\n 5. Main Work", 'green')
print(option_text)

input_text = colored("\nPlease enter option : ", 'green')
option = int(input(input_text))

print(constants.SPACE)

#########Options##########

if option == 1:

    print("Step 1: Check if Virtualization is supported in Ubuntu.\n")
    print("\tcommand: egrep -c \'(vmx|svm)\' /proc/cpuinfo")
    print("\tIf outcome greater than 0 then virtualization is supported. Next check if KVM virtualization is upported.")
    print("\tcommand: sudo kvm-ok")

    note = colored("\tNote: If \'kvm-ok\' utility is not present in system use following command: sudo apt install cpu-checker", "red")
    print(note)

    print("Step 2: Installing KVM\n")
    print("\tcommand: sudo apt install -y qemu qemu-kvm libvirt-daemon libvirt-clients bridge-utils virt-manager\n")
    cprint("\tExplanation of command: \n", "magenta")
    explanation = colored("\t1. qemu package (quick emulator) is an application that allows you to perform hardware virtualization.\n\t2. qemu-kvm package is the main KVM package.\n\t3. The libvritd-daemon is the virtualization daemon\n\t4. bridge-utils package helps you create a bridge connection to allow other users to access a virtual machine other than the host system.\n\t5. virt-manager is an application for managing virtual machines through a graphical user interface\n", "magenta")
    print(explanation)

    print("\tConfirm that virtualization daemon, libvritd-daemon, is running.")
    print("\tCommand: sudo systemctl status libvirtd\n")

    print("\tEnable program.")
    print("\tCommand: sudo systemctl enable --now libvirtd\n")

    print("\tCheck if KVM module is loaded.")
    print("\tCommand: lsmod | grep -i kvm\n")

#

elif option == 2:

    print("There are two options to create a VM.")
    print("1. Command Line")
    print("\tCommand: sudo virt-install --name=deepin-vm --os-variant=Debian10 --vcpu=2 --ram=2048 --graphics spice --location=/home/Downloads/deepin-20Beta-desktop-amd64.iso --network bridge:vibr0")
    cprint("\tExplanation of command: \n", "magenta")
    print("\t1. --name is name of VM\n\t2. --os-variant indicates the OS family\n\t3. --vcpu indicates CPU cores\n\t4. --ram indicates RAM capacity\n\t5. --location flag points to the aboslute path of ISO image\n\t6. --network bridge specifies adapter to be used by VM.\n")

    print("2. Using GUI")
    print("\tSimply run the command \"virt-manager\"\n")
    print("\tWhen GUI pops up, click on monitor icon.")

    cprint("\tError!", "red")
    cprint("\tIf encountered with the error \"no active connection to install on\", then make sure you are running the above command with sudo.\n", "red")

    print("\tChose the option \"Local install media(ISO image or CDROM)\" and then click the \'Forward\' button.")
    print("\tBrowse for the iso image of the Linux distro that you want to add. Chose the OS by typing it in and selecting the appropriate option. (Deselect the automatic detection option). Click the \'Forward\' button")

    print("\tChose the amount of memory you want to allocate and the number of CPU cores you want to use for you VM. Click the \'Forward\' button")

    print("\tChose the option to enable storage for the VM nad chose the size for the disk image. Click the \'Forward\' button.")
    cprint("\t(The above step may be pertinent to the newer version of KVM.)", "cyan")
    print("\tFinally, name your VM, check all of the settings that you have made for your VM, and click on the \'Finish\' button to end the set up process.")

#

elif option == 3:

    print("I chose the Parrot OS Linux distro because I wanted to try something different from Kali and Ubuntu. ¯\_(ツ)_/¯")

    print("So, to setup Parrot OS is pretty simple. As soon as the GNU/GRUB boots up, simply select the \'Try/Install\' option.")
    print("Then click on the \'Install Parrot\' desktop icon.")
    print("The steps after this are pretty direct.\n\tYou need to simply change the location according to your needs (Change the language for the time as well!).\n\tFor the partitions option, you can chose to have the full disk wiped out or do manual partitioning. Since I am using a fresh VM, it really doesn't make a difference right now.\n\tCreate your own username and password, and change any of the details as per your liking.\n\tFinally, go through the summary, and make any changes that you deem necessary. If you are happy with the details and options you have chosen, simply click on install, wait for the OS to install and then click on finish. The OS will reboot and cliking on the first option in the GNU/GRUB, you can now use Parrot OS without having to worry about the following error :)")
    cprint("\t\tBoot failed:  not a bootable disk", "red")

#

elif option == 4:

    initial_string = f"Before beginning with the nitty-gritty, there are a few things to keep in mind. We wil be setting up a minimum of {Fore.BLUE}3{Style.RESET_ALL} VMs. This can be increased depending on the requirements."

    print(initial_string)

    print("Also note, I am a complete noob in this domain, and this is just a learning project. :)")

elif option == 5:

    print("Select the following sub topics: ")
    print("a. Setting Static IP Address\nb. freeIPA")
    option = input("Enter the option: ")

    if option == 'a':
        print("This was a really tough one (╥_╥). I was especially reluctant because my team members had tried to do so in our IoT project. We had failed miserably. But now, after a whole day of dead ends and raging, I finally got this done. I'll go through the processes of how I went about with getting the IP address changed from dynamic to static.")

        print("The most obvious thing is to use the google search engine. I found a similar method in most of the websites and videos, which is as follows.")
        print("The tutorials I searched for were realted to Debian/Ubuntu based Linux Distros.")
        print("Simply open the cli and type in the following command: ")
        print("\tvi /etc/network/interfaces")
        cprint("Note: Root access maybe requried to access the interfaces file. You might have to change the permissions as well, because the file was read-only even after root access for me.")
        print("In most of the tutorials the following lines (or a variation of it), are supposed to be mentioned in the interfaces folder.")
        print("\tauto eth0\n\tiface eth0 inet dhcp")
        print("But for me, they were missing. So, simply add the following lines in place of the ones above.")
        print("\tauto eth0\n\tiface eth0 inet static\n\taddress 192.168.0.100\n\tnetmask 255.255.255.0\n\tgateway 192.168.0.1\n\tdns-nameserver 208.67.222.222 208.67.220.220")

        print("After entering this information, simply save the file and then reboot the system.")
        print("Voila! Congratulations, you just permanentaly disabled your connection! ಥ◡ಥ)")
        print("So, I was left confused on as to why this was happening. It seemed to be working really well for the people who showed this in the tutorials.")
        print("So, I kept on digging and trying new things and finally happened to come across a god-sent tutorial. Just directly check it out, it explains things pretty clearly and me explaining it isn't gonna make a difference.")

        print("Link: https://tqdev.com/2020-kvm-network-static-ip-addresses")

        extra_string = f"Extra information {Fore.RED}\"your VM is a guest machine of your Host operating system, and as such has no direct connection to the outside world, but uses bridging to connect through the host system, this creates a “wired connection” and so ,shows as such in the VM, control over the Wi-Fi connections remain the responsibility of the host system and so any changes have to be made there.\"{Style.RESET_ALL} "
        print(extra_string)
        print("In simple terms, the network built-in laptop/pc becomes ethernet interface in VM guest OS and the host machine.")
