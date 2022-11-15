<!DOCTYPE html>
<html>
<head> 
<meta charset="utf-8">
<title>안서동 맛집 정보 카페</title>
<link rel="stylesheet" type="text/css" href="./css/project_main.css">
<script>
  function check_input() {
      if (!document.login_form.pass.value)
      {
          alert("제목을 입력하세요!");
          document.login_form.pass.focus();
          return;
      }
      document.login_form.submit();
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
  
        <div id="main_content">
      		<div id="login_box">
	    		<div id="login_title">
		    		<span>회원 정보를 수정하려면 비밀번호 재입력이 필요합니다!</span>
	    		</div>
	    		<div id="login_form">
          		<form  name="login_form" method="post" action="member_modify_pass.php?id=<?=$userid?>">		       	
                  	<ul>
                    <?php
                      
                    ?>
                    <li>
                      <span class="col1">아이디 : </span>
                      <span class="col2"><?=$userid?></span>
                    </li>
                    <li><input type="password" id="pass" name="pass" placeholder="비밀번호" ></li> <!-- pass -->
                  	</ul>
                  	<div id="login_btn">
                      	<a href="#"><img src="./img/login.png" onclick="check_input()"></a>
                  	</div>		    	
           		</form>
        		</div> <!-- login_form -->
    		</div> <!-- login_box -->
        </div> <!-- main_content -->
	</section> 
	<footer>
    	<?php include "footer.php";?>
    </footer>
</body>
</html>