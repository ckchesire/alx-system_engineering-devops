# Script used to kill process initiated by killmenow bash file
exec { 'killmenow':
   command  => '/usr/bin/pkill killmenow',
   provider => 'shell',
   returns  => [0, 1],
}
