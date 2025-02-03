# UFW (Uncomplicated Firewall) Guide

## What is a Firewall?
A **firewall** is a security tool that controls incoming and outgoing network traffic based on security rules. It protects systems from unauthorized access and cyber threats.

## Why Use a Firewall?
- Blocks unauthorized access to your system.
- Prevents cyber attacks and malware.
- Controls network traffic and enforces security policies.
- Improves network performance and monitoring.

## What is UFW?
`UFW` (Uncomplicated Firewall) is a user-friendly firewall for Linux, mainly used on Ubuntu and Debian systems. It simplifies firewall rule management.

## Installing UFW
```bash
sudo apt update && sudo apt install ufw -y
```

## Basic UFW Commands
### Check Status:
```bash
sudo ufw status
```

### Set Default Policies:
```bash
sudo ufw default deny incoming
sudo ufw default allow outgoing
```

### Allow Essential Ports:
```bash
sudo ufw allow 22/tcp   # SSH
sudo ufw allow 80/tcp   # HTTP
sudo ufw allow 443/tcp  # HTTPS
```

### Enable UFW:
```bash
sudo ufw enable
```

### Verify Rules:
```bash
sudo ufw status verbose
```

### Deny Specific Port:
```bash
sudo ufw deny 8080
```

### Remove a Rule:
```bash
sudo ufw delete allow 80/tcp
```

### Disable UFW:
```bash
sudo ufw disable
```

### Reset UFW:
```bash
sudo ufw reset
```

## Conclusion
UFW is a simple yet effective tool for securing Linux servers. It helps manage firewall rules easily while protecting against unauthorized access.
