# Solves wordpress config issue, changing "phpp" to "php" in "wp-settings.php"
exec {'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}

