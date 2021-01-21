
2021-01-20 23:52:09

setup-ec2-instance-ansible-lab.sh

EDEN: These are the steps I followed on setting up the AWS EC2 instances for the ansible lab.

1. Created a VPC, a subnet, route table, and an internet gateway dedicated for the lab.

2. Change default username of all EC2 instances during instance creation. This is to make sure I have a username with root privileges on all 3 linux machine. Check out the steps in this file:

changing_default_system_username_ec2.txt 

3. Set password for the username.

4. Change hostnames of each EC2 instance according to the ansible lab.

5. Set 'PasswordAuthentication yes' in /etc/ssh/sshd_config in all 3 linux machines.