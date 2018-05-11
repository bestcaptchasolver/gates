#!/usr/bin/python2.7
import os
import sys

OS_NOTIF = True      # notify-send notification

# notification for archlinux (more exactly for notify-send)
def notify_send(msg):
    os.system('notify-send Hosts "{}"'.format(msg))

# toggle - enable / disable hosts file for given IP and domain
def toggle(ip, domain):
    status = False
    hosts_file_content = ''
    new_lines = []
    temp = '/tmp/hosts_captcha'
    with open('/etc/hosts') as f:  lines = f.read()
    for line in lines.splitlines(): 
        line = line.strip()
        # check if enabled
        if not line.startswith("#") and ip in line and domain in line: status = True
        elif (ip not in line and domain not in line): new_lines.append(line)

    # if it wasn't enabled, enable (add line to list)
    if not status: new_lines.append('{}    {}'.format(ip, domain))

    # write to temp file
    with open(temp, 'w') as f:
        for l in new_lines:  f.write('{}\n'.format(l))
    # move to real hosts file
    cmd = 'sudo mv {} /etc/hosts'.format(temp)
    os.system(cmd)
    os_notif = ''
    if status: 
        print '[+] disabled'
        os_notif = '#{}  {} - disabled'.format(ip, domain)
    else: 
        print '[+] enabled'
        os_notif = '{}  {} - enabled'.format(ip, domain)

    # 'pretty' notification for notify-send
    if OS_NOTIF: notify_send(os_notif)

def main():
    # check arguments length
    if len(sys.argv) < 3:
        print '[+] Usage: ./linux_hosts.py 127.0.0.1 google.com'
        return

    toggle(sys.argv[-2], sys.argv[-1])  # toggle

main()
