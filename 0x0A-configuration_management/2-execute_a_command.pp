# create a manifext that kills a process killmenow
exec { 'pkill':
  command  => 'pkill killmenow',
  provider => 'shell',
}
