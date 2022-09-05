echo "Enter port number"

read num

if ! [[ "$num" =~ ^[0-9]+$ ]]
then
	echo "Sorry integers only"
	exit 0
fi

if [ "$num" -gt 32767 ] || [ "$num" -le 1024 ]
then
	echo "Port number must be between 1024 and 32767"
	exit 0
fi


# Change Port
$FILE = "/etc/ssh/sshd_config"

if grep -q "#Port 22" $FILE;
then
	sed 's/#Port 22/Port $num/' $FILE
else
	sed 's/Port .*/Port $num/' $FILE
fi


# Allow traffic on the new SSH port
sudo firewall-cmd --permanent --zone=public --add-port="$num"/tcp
sudo firewall-cmd --reload

# Adjust SELinux rules
sudo semanage port -a -t ssh_port_t -p tcp "$num"

# Restart sshd
sudo systemctl restart sshd

# Disable root login
sed 's/#PermitRootLogin yes/PermitRootLogin no/' $FILE


# Check if at least one user has sudo privilege 
if [[ $(grep '^sudo:.*$' /etc/group) ]]; then
    echo "there exist sudo users"
else
    echo "there are no sudo users"
fi
