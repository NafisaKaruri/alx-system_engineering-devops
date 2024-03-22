# create a manifext that kills a process killmenow
exec { 'pkill':
  command => 'pkill -9 -f killmenow',
  path    => {'/usr/bin', '/usr/sbin', '/bin'}
}
