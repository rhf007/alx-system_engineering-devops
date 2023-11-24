# kill me now
exec { 'kill':
  command  => 'pkill killmenow',
  provider => 'pkill',
}
