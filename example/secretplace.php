<?php
  session_start();
  if(!isset($_SESSION['logged_user'])){
    header("Location: index.php");
    exit;
  }
?>
<html>
 <body>
    <div id="main_menu">
       <ul>
           <li><a href="main_menu_link1.php">link1</a></li>
           <li><a href="main_menu_link2.php">link2</a></li>
           <li><a href="main_menu_link3.php">link3</a></li>
           <li><a href="main_menu_link4.php">link4</a></li>
       </ul>
    </div>
     
    <div id="left_sidebar" style="float: left">
        <li><a href="left_sidebar_link1.php">left_sidebarlink1</a></li>
        <li><a href="left_sidebar_link2.php">left_sidebar_link2</a></li>
        <li><a href="left_sidebar_link3.php">left_sidebar_link3</a></li>
        <li><a href="left_sidebar_link4.php">left_sidebar_link4</a></li>
    </div>

     <div id="page">
         <h3>Main Content</h3>
     </div>
 </body>
</html>