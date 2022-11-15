<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>안서동 맛집 정보 카페</title>
    <link rel="stylesheet" type="text/css" href="./project_main.css">
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
    <div id="star_box">
        <h3 id="star_title">
            방문해보신 식당을 별점으로 평가해주세요!
        </h3>
        <form name="star_form" method="post" action="star_insert.php" enctype="multipart/form-data">
            <ul id="star_form">
            <li>
            <span class="col1">식당 선택하기 : </span>
                <select name="res">
                    <option value="쌍용식당">쌍용식당</option>
                    <option value="용우동">용우동</option>
                    <option value="이슬목장">이슬목장</option>
                    <option value="정가네닭갈비">정가네 닭갈비</option>
                    <option value="앗싸양꼬치">앗싸 양꼬치</option>
                    <option value="코코스낵">코코스낵</option>
                </select>
            <span class="col2">별점 매기기 : </span>
                <select name="star">
                    <option value="1">★</option>
                    <option value="2">★★</option>
                    <option value="3">★★★</option>
                    <option value="4">★★★★</option>
                    <option value="5">★★★★★</option>
                </select>
            </li>            
            <li><button type="button" onclick="check_input()">완료</button></li>
        </form>
</div>
    <div id="main_content">
<?php
    $con = mysqli_connect("localhost", "user1", "12345", "projectsample");
?>
<div id="star_rank">
    <h4>내가 매긴 맛집 평점
        <ul>
<!-- 포인트 랭킹 표시하기 -->
<?php
    $sql = "select * from star order by num desc";
    $result = mysqli_query($con, $sql);

    if (!$result)
        echo "맛집 DB 테이블(star)이 생성 전이거나 아직 평가된 맛집이 없습니다!";
    else
    {
        while( $row = mysqli_fetch_array($result) )
        {
            $restaurant  = $row["restaurant"];        
            $star    = $row["resstar"];
?>
                <li>
                    <span><?=$restaurant?> : </span>
                    <span><?=$star?></span>
                </li>
<?php
        }
    }

    mysqli_close($con);
?>
                </ul>
            </div>          
</div>
    </section>
    <footer>
        <?php include "footer.php";?>
    </footer>
</body>
</html>