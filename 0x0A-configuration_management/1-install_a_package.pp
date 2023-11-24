# installing a package
package { 'flask':
  ensure => 'installed',
  install_options =>  ['-v', '2.1.1'],
}
