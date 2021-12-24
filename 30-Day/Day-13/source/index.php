<html>

<head>
    <title>BigNumber</title>
    <link rel='stylesheet' href='style.css' type='text/css'>
</head>

<body>

    <?php
    require 'flag.php';

    if (isset($_GET)) {
        if (is_numeric($_GET['too'])) {
            if (strlen($_GET['too']) < 4) {
                if ($_GET['too'] > 999) die('Flag: ' . $flag);
                else print '<p class="alert">Baga bna, Tom Bai</p>';
            } else print '<p class="alert">Tom bna, Baga bai</p>';
        } else print '<p class="alert">No Number, No Cry</p>';
    }

    ?>

    <section class="login">
        <form method="get">
            <input type="text" required name="too" placeholder="Numbers Only" /><br />
            <input type="submit" />
        </form>
    </section>
</body>

</html>