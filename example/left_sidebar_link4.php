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
        <li><a class="side" href="left_sidebar_link1.php">left_sidebarlink1</a></li>
        <li><a class="side" href="left_sidebar_link2.php">left_sidebar_link2</a></li>
        <li><a class="side" href="left_sidebar_link3.php">left_sidebar_link3</a></li>
        <li><a class="side" href="left_sidebar_link4.php">left_sidebar_link4</a></li>
    </div>

     
        <frameset rows="40,*,32"  frameborder="0" framespacing="0" >
            <iframe width="545" height="438" src="body4.html"></iframe>
        </frameset>
    </div>
 </body>
</html>