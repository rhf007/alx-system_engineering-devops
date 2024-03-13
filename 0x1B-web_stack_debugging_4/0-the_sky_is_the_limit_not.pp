exec { 'set limit to 2000':
  path    => '/bin',
  command => "sed -i 's/15/2000/' /etc/default/nginx"
}

exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
