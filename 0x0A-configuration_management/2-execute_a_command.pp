# Script used to kill process initiated by killmenow bash file
exec { 'pkill':
   command  => '/usr/bin/pill killmenow',
   provider => 'shell',
}
