# Fix why Apache is returning a 500 error

exec { 'fix':
  command => ''sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
