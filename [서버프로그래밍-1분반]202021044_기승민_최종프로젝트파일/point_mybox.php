<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>안서동 맛집 정보 카페</title>
    <link rel="stylesheet" type="text/css" href="./css/project_main.css">
    <script>
    function check_input() {
      document.star_form.submit();
   }
   </script>
</head>
<body>
<header>
        <?php include "header.php";?>
    </header>
    <nav>
        <?php include "nav.php";?>
    </nav>
    <section>
    
    
<?php
    $con = mysqli_connect("localhost", "user1", "12345", "projectsample");
?>
<div id="point_box">
    <h3>맛집 서비스 쿠폰 사기 | <a href="point_form.php">쿠폰 더 사러가기</a></h3>	    
        <ul>

<?php
    $sql = "select * from service order by num desc";
    $result = mysqli_query($con, $sql);

    if (!$result)
        echo "서비스 쿠폰 DB 테이블(service)이 생성 전이거나 아직 구매된 서비스 쿠폰이 없습니다!";
    else
    {
        while( $row = mysqli_fetch_array($result) )
        {
            $coupon  = $row["coupon"]; 
            if ($coupon == "res1")
            {
?>
<span>
                <li><img src="./img/res1service.png"></li>
<?php
                $coupon_name = "쌍용식당";
?>
                <li><?=$coupon_name?></li>
            </span>
<?php
            }
            if ($coupon == "res2")
            {
?>
<span>
                <li><img src="./img/res2service.png"></li>
<?php
                $coupon_name = "이슬목장";
?>
                <li><?=$coupon_name?></li>
                </span>
<?php
            }
            if ($coupon == "res3")
            {
?>
<span>
                <li><img src="./img/res3service.png"></li>
<?php
                $coupon_name = "정가네닭갈비";
?>
                <li><?=$coupon_name?></li>
                </span>
<?php
            }
            if ($coupon == "res4")
            {
?>
<span>
                <li><img src="./img/res4service.png"></li>
<?php
                $coupon_name = "용우동";
?>
                <li><?=$coupon_name?></li>
                </span>
<?php
            }
            if ($coupon == "res5")
            {
?>
<span>
                <li><img src="./img/res5service.png"></li>
<?php
                $coupon_name = "앗싸양꼬치";
?>
                <li><?=$coupon_name?></li>
                </span>
<?php
            }
            if ($coupon == "res6")
            {
?>
<span>
                <li><img src="./img/res6service.png"></li>
<?php
                $coupon_name = "코코스낵";
?>
                <li><?=$coupon_name?></li>
                </span>
<?php
            }
            
      
?>
                
<?php
        }
    }

    mysqli_close($con);
?>
                </ul>
            </div>          

    </section>
    <footer>
        <?php include "footer.php";?>
    </footer>
</body>
</html>