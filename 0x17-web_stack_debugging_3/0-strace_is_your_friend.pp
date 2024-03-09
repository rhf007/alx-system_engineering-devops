#fixing apache 500 error

exec { 'fixerror':
  path     => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
  command  =>  "sed -i 's/.phpp/.php/g' /var/www/html/wp-settings.php",
  provider =>  'shell'}
