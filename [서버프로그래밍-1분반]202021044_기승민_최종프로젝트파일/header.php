<?php
    session_start();
    if (isset($_SESSION["userid"])) $userid = $_SESSION["userid"];
    else $userid = "";
    if (isset($_SESSION["username"])) $username = $_SESSION["username"];
    else $username = "";
    if (isset($_SESSION["userlevel"])) $userlevel = $_SESSION["userlevel"];
    else $userlevel = "";
    if (isset($_SESSION["userpoint"])) $userpoint = $_SESSION["userpoint"];
    else $userpoint = "";
?>
	
        <div id="top">
            <h3>
                <a href="index.php">안서동 맛집 정보 카페</a>
            </h3>
            <ul id="top_menu">   
<?php
    if(!$userid) {
?>                
                <li><a href="member_form.php">회원 가입</a> </li>
                <iframe src="login_form.php" width="450" height="200">
                </iframe>
<?php
    } else {
                $logged = $username."(".$userid.")님[Level:".$userlevel."]";
?>
                <li><?=$logged?> </li>
                <li> | </li>
                <li><a href="logout.php">로그아웃</a> </li>
                <li> | </li>
                <li><a href="member_modify_pass_form.php">정보 수정</a></li>
<?php
    }
?>
<?php
    if($userlevel==9) {
?>
                <li> | </li>
                <li><a href="admin.php">관리자 모드</a></li>
<?php
    }
?>
            </ul>
        </div>

