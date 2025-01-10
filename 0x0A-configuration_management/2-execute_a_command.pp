# Script used to kill process initiated by killmenow bash file
exec { 'pkill':
   command  => '/usr/bin/pkill killmenow',
   provider => 'shell',
}
