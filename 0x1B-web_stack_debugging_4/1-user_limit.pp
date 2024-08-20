# increase holberton user limits

exec { 'increase hard file limit 4 -> 50000':
  command => 'sed -i "/holberton hard/s/4/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

exec { 'increase soft file limit 5 -> 50000':
  command => 'sed -i "/holberton soft/s/5/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

