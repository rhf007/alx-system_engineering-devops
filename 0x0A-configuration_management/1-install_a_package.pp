# installing a package
package { 'flask':
 command => '/usr/bin/pip3 install flask==2.1.0',
}

package { 'Werkzeug':
  command => '/usr/bin/pip3 install werkzeug==2.1.1',
}
