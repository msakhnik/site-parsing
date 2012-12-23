<?php
  session_start();
  if($_POST['user_pass']){
    if($_POST['user_pass'] == 'password' && $_POST['user_name'] == 'user'){
      $_SESSION['logged_user'] = '{' . $_POST['user_name'] . '}';
      echo "1";
      header("Location: secretplace.php");
      exit;
    }
  }
  // если что-то было не так, то пользователь получит
  // сообщение об ошибке.
?>
<html><body>
Wrong password
</body></html>