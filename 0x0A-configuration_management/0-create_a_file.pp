# creating a file
file { '/tmp/school':
  ensure  => 'present',
  path    => '/tmp/school',
  content => 'I love Puppet',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
}
