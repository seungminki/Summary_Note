<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>안서동 맛집 정보 카페</title>
    <link rel="stylesheet" type="text/css" href="./css/project_main.css">
</head>
<body>
    <header>
        <?php include "header.php";?>
    </header>
    <nav>
	<?php include "nav.php";?>
    </nav>
    <?php
	if (!$userid )
	{
		echo("<script>
				alert('로그인 후 이용해주세요!');
				history.go(-1);
				</script>
			");
		exit;
	}
?>
    <section>
        <div id="point_box">
            <h3 id="write_title">맛집 서비스 쿠폰 사기 | <a href="point_mybox.php">내 쿠폰함</a></h3>
        <form  name="point_form" method="post" action="point_insert.php?id=<?=$userid?>"> 
            <span>
            <li><img src="./img/res1service.png"></li>
            <li><button onclick="location.href='point_insert.php?coupon=res1'">2000원에 사기</button></li>
            </span>

            <span>
            <li><img src="./img/res2service.png"></li>
            <li><button onclick="location.href='point_insert.php?coupon=res2'">1000원에 사기</button></li>
            </span>

            <span>
            <li><img src="./img/res3service.png"></li>
            <li><button onclick="location.href='point_insert.php?coupon=res3'">2000원에 사기</button></li>
            </span>

            <span>
            <li><img src="./img/res4service.png"></li>
            <li><button onclick="location.href='point_insert.php?coupon=res4'">3000원에 사기</button></li>
</span>
            
            <span>
            <li><img src="./img/res5service.png"></li>
            <li><button onclick="location.href='point_insert.php?coupon=res5'">3000원에 사기</button></li> 
            </span>

            <span>
            <li><img src="./img/res6service.png"></li>
            <li><button onclick="location.href='point_insert.php?coupon=res6'">1000원에 사기</button></li>
            </span>
        </form>
        
        </div>
    </section>
    <footer>
        <?php include "footer.php";?>
    </footer>
</body>
</html>