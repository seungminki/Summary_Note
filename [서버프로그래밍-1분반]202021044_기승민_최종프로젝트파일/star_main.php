<link rel="stylesheet" type="text/css" href="./project_main.css">
<div id="main_content">
<?php
    $con = mysqli_connect("localhost", "user1", "12345", "projectsample");
?>
<div id="star_rank">
    <h4>실시간 맛집 평점 순위</h4>
        <ul>
<!-- 포인트 랭킹 표시하기 -->
<?php
    $rank = 1;
    $sql = "select * from star order by resstar desc limit 5";
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
                    <span><?=$rank?></span>
                    <span><?=$restaurant?></span>
                    <span><?=$star?></span>
                </li>
<?php
            $rank++;
        }
    }

    mysqli_close($con);
?>
                </ul>
            </div>          
</div>