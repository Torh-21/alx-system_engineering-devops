# Fixed the limit in nginx default file
exec { 'changeLimit':
    command => 'sed -i "s/15/4096/g" /etc/default/nginx; service nginx restart',
    path    => '/usr/bin/:/bin/',
}
