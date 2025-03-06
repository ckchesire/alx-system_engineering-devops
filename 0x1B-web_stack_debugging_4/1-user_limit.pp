# Puppet file to enable user 'Holberton' to login and open files without error

# Increase the hard file limit for user 'Holberton'
exec { 'increase-hard-file-limit-for-user-holberton':
  command => "sed -i '/^holberton hard/s/4/50000/' /etc/security/limits.conf",
  path    => '/usr/local/bin/:/bin/'
}

# Increase the soft file limit for user 'Holberton'
exec { 'increase-soft-file-limit-for-user-holberton':
  command => 'sed -i "/^holberton soft/s/5/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
