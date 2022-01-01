<?php 
$flag = "ccsCTF{y0u_@r3_h@ck3r}";
if (isset($_POST['email'])) {
   $email = $_POST['email'];
   $pass = $_POST['pass'];
   if ($email == "sict.ccsclub@gmail.com" && $pass == "security" ){
        echo '<h1 style="color:red">'.$flag.'</h1>';
   }
   else {
        header('Location: index.php?error=incorrect');
   }


}
