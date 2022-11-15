<meta charset="utf-8">
<?php
    session_start();
    if (isset($_SESSION["userid"])) $userid = $_SESSION["userid"];
    else $userid = "";

    if (!$userid)
    {
        echo("
        <script>
            alert('식당 별점 매기기는 로그인 후 이용해 주세요!');
            history.go(-1)
        </script>
        ");
        exit;
    }
    $restaurant = $_POST["res"];
    $star = $_POST["star"];

    $restaurant = htmlspecialchars($restaurant, ENT_QUOTES);
    
    $con = mysqli_connect("localhost", "user1", "12345", "projectsample");
    $sql = "insert into star (id, restaurant, resstar) ";
    $sql .= "values('$userid', '$restaurant', '$star')";
    mysqli_query($con, $sql);

    $point_up = 50;
    $sql = "select point from members where id='$userid'";
    $result = mysqli_query($con, $sql);
    $row = mysqli_fetch_array($result);
    $new_point = $row["point"] + $point_up;

    $sql = "update members set point=$new_point where id='$userid'";
    mysqli_query($con, $sql);

    mysqli_close($con);

    echo "
    <script>
        location.href = 'star.php';
    </script>
    ";
?>