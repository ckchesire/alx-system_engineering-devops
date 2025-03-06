# Puppet file to increase the amout of traffic nginx server can handle

# Run executable to increase the ULIMIT of the default file
exec { 'update_for_nginx':
  # Update the ULIMIT value
  command => '/bin/sed -i "s/15/4096/" /etc/default/nginx',
  # Specify the particular path for the sed command
  path => '/usr/local/bin/:/bin/',
}

# Restart the Nginx server
exec { 'nginx_server_restart':
  # Restart the Nginx service
  command => '/etc/init.d/nginx restart',
  # Specify the absolute path for the init.d script
  path => '/etc/init.d/',
}
