<html>

<body>
    <?php
    $servername = "localhost";
    $username = "root";
    $password = "password";
    $port = 3307;
    $conn = new mysqli($servername, $username, $password, $port);
    //$query = "SELECT * FROM FLAG.SQLI;"
    //echo $query;
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }
    ?>
    <?php
    // $sql = "SELECT * FROM FLAG.sqli where name = 'ulmaa'"; 
    $name = $_POST["name"];
    $email = $_POST["email"];
    $sql = "SELECT * FROM FLAG.sqli WHERE name = $name";
    $result = $conn->query($sql);

    if ($result->num_rows > 0) {
        // output data of each row
        while ($row = $result->fetch_assoc()) {
            echo $row['email'] . "<br>";
        }
        die("WELL DONE");
    }
    echo "HELLO " . $name . "<br>";
    echo "i sent you a new year's gift to your " . $email;
    ?>
</body>

</html>