<meta charset="utf-8">
<?php
	session_start();
    if (isset($_SESSION["userid"])) $userid = $_SESSION["userid"];
    else $userid = "";

	$coupon = $_GET["coupon"];

    if (!$userid)
    {
        echo("
        <script>
            alert('서비스 쿠폰 구매는 로그인 후 이용해 주세요!');
            history.go(-1)
        </script>
        ");
        exit;
    }

	if ($coupon=="res1")
    {
	    $point_down = 2000;
	    $usercoupon = "res1";
	}
	if ($coupon=="res2")
    {
	    $point_down = 1000;
        $usercoupon = 'res2';
	}
	if ($coupon=="res3")
    {
	    $point_down = 2000;
        $usercoupon = 'res3';
	}
	if ($coupon=="res4")
    {
	    $point_down = 3000;
        $usercoupon = 'res4';
	}
	if ($coupon=="res5")
    {
	    $point_down = 3000;
        $usercoupon = 'res5';
	}
	else 
	{
		$point_down = 1000;
        $usercoupon = 'res6';
	}

	$con = mysqli_connect("localhost", "user1", "12345", "projectsample");
    $sql = "insert into service (id, coupon) ";
    $sql .= "values('$userid', '$usercoupon')";
    mysqli_query($con, $sql);

	$sql = "select point from members where id='$userid'";
    $result = mysqli_query($con, $sql);
    $row = mysqli_fetch_array($result);
    $new_point = $row["point"] - $point_down;
    $sql = "update members set point=$new_point where id='$userid'";
    mysqli_query($con, $sql);

    mysqli_close($con);

    echo "
    <script>
        location.href = 'point_mybox.php';
    </script>
    ";
?>