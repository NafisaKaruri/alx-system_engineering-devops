# Custom HTTP header in a nginx server

# update ubuntu system
exec { 'update system':
  command  => '/usr/bin/apt-get update',
}

# install nginx web server
package { 'nginx':
  ensure   => 'installed',
}

# custom Nginx response to Hello World!
file { '/var/www/html/index.html':
  content => 'Hello World!',
}

# custom Nginx response header (redirect_me: youtubelink)
exec { 'redirect_me':
  command  => 'sed -i "24i\	rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" /etc/nginx/sites-available/default',
  provider => 'shell'
}

# custom Nginx response header (X-Served-By: hostname)
file_line { 'add HTTP header':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'add_header X-Served-By $hostname;'
}

# start service
service { 'nginx':
  ensure  => 'running',
  require => Package['nginx']
}
