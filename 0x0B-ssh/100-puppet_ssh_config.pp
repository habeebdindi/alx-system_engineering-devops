# edits ssh_config file
file { '/etc/ssh/ssh_config':
  ensure  => 'file',
  content => '
    Host 54.87.180.247
        IdentityFile ~/.ssh/school
        PasswordAuthentication no
  ',
  owner   => 'vagrant',
  group   => 'vagrant',
  mode    => '0600',
}
