
import subprocess


def copy_to_clipboard(txt):
    # This is probably Windows only, could use pyperclip but not relying on external non-standard libs in this so far
    cmd = 'echo ' + txt.strip() + ' | clip'
    try:
        subprocess.check_call(cmd, shell=True)
        print("save location path is copied to your clipboard (control+v it into Jira!)")
    except:
        print("failed to copy to clipboard, what OS is this?")


if __name__ == '__main__':
    copy_to_clipboard("M0ntana")

    # scp_command += ' -pw=M0ntana -r '
    # scp_command += ' -pwfile superman ' # DOES NOT SEEM TO WORK
    # scp_command += ' -pw M0ntana '
    #scp_command = "scp -r root@172.16.255.30:/var/lib/calrec/log/live ."
    #scp_command = "scp -pw M0ntana root@172.16.255.30:/var/lib/calrec/log/live ."
    #scp_command = "scp PeterW@192.168.1.14:\\Users\\PeterW\\Documents\\ ."
    scp_command = "pscp -ls peterw@192.168.1.14"
    subprocess.check_output(scp_command)

