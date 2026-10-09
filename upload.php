<?php
// Intentionally vulnerable PHP for SAST testing. Do not deploy.

// Path traversal + unrestricted file include: user controls the path
$page = $_GET['page'];
include($page . ".php");

// Reflected XSS: input echoed back without encoding
$name = $_GET['name'];
echo "<h1>Welcome " . $name . "</h1>";

// Local file read via traversal
$file = $_GET['file'];
echo file_get_contents("/var/www/uploads/" . $file);
?>
