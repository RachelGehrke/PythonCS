import socket
import os

# Define the main function for the firewall rules configuration
def configure_firewall():
    # Define the rules array. Each rule is a dict with 'action', 'protocol', 'port' and 'ip' keys
    rules = [
        {'action': 'allow', 'protocol': 'tcp', 'port': 80, 'ip': 'any'},   # Allow HTTP traffic
        {'action': 'allow', 'protocol': 'tcp', 'port': 443, 'ip': 'any'},  # Allow HTTPS traffic
        {'action': 'deny', 'protocol': 'tcp', 'port': 22, 'ip': 'any'}     # Deny SSH traffic from all IPs
    ]

    # Function to add a firewall rule
    def add_rule(action, protocol, port, ip):
        # Generate the iptables command
        rule_command = f'iptables -{'A' if action == 'allow' else 'D'} INPUT -p {protocol} --dport {port}'
        # Add the IP address if specified
        if ip != 'any':
            rule_command += f' -s {ip}'
        # Finalize the rule with an action
        rule_command += f' -j {'ACCEPT' if action == 'allow' else 'REJECT'}'
        # Execute the command
        os.system(rule_command)
        print(f'Rule added: {rule_command}')

    # Configure the firewall based on the rules array
    for rule in rules:
        add_rule(rule['action'], rule['protocol'], rule['port'], rule['ip'])

# If executed as the main program, configure the firewall
if __name__ == '__main__':
    configure_firewall()