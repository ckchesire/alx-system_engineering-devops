# Puppet file to increase the amout of traffic nginx server can handle

# Run executable to increase the ULIMIT of the default file
exec { 'fix-for-nginx':
  # Update the ULIMIT value
  command => 'sed -i "s/15/4096/" /etc/default/nginx && sudo service nginx restart',
  # Specify the particular path for the sed command
  path    => '/usr/local/sbin/:/usr/local/bin/:/usr/sbin:/usr/bin:/sbin:/bin'
}
