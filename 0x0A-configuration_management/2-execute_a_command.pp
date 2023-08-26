#kills a process
exec {'kill_killmenow_proc':
  command => 'pkill killmenow',
  path    => '/usr/bin:/usr/sbin:/bin:/sbin',
  onlyif  => 'pgrep killmenow',
}
