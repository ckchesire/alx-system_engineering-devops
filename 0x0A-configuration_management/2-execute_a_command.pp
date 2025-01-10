# Script used to kill process initiated by killmenow bash file
exec { 'pkill':
   command  => 'pkill killmenow',
   provider => 'shell',
}
