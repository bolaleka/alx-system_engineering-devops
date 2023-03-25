# Create a file in tmp with permission 

file { '/tmp/school':
    content => 'I love Puppet'
    mode    => '0744',
    owner   => 'www-data',
    group   => 'www-data',
}
