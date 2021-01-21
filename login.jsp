<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
    <% request.setCharacterEncoding("EUC-KR");%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=EUC-KR">
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <meta name="author" content="">
    <title>Sign up</title>
    <link href="css/bootstrap.min.css" rel="stylesheet">
    <link href="css/font-awesome.min.css" rel="stylesheet">
    <link href="css/prettyPhoto.css" rel="stylesheet">
    <link href="css/price-range.css" rel="stylesheet">
    <link href="css/animate.css" rel="stylesheet">
	<link href="css/main.css" rel="stylesheet">
	<link href="css/responsive.css" rel="stylesheet">
    <script src="js/jquery.js"></script>
	<script src="js/bootstrap.min.js"></script>
	<script src="js/jquery.scrollUp.min.js"></script>
	<script src="js/price-range.js"></script>
    <script src="js/jquery.prettyPhoto.js"></script>
    <script src="js/main.js"></script>
</head><!--/head-->


<body>
<header id="header"><!--header-->
		<div class="header_top"><!--header_top-->
			<div class="container">
				<div class="row">
					<div class="col-sm-6">
						<div class="contactinfo">
							<ul class="nav nav-pills">
								<li><a href="#"></i> 클라우드 컴퓨팅 기말과제</a></li>
								<li><a href="#"></i> 팀장: 홍석찬 팀원: 손현곤 , 박신형</a></li>
							</ul>
						</div>
					</div>
				
				</div>
			</div>
		</div><!--/header_top-->
		
	<!--form-->
		<div class="container">
			<div class="row">
				<div class="col-sm-4 col-sm-offset-1">
					<div class="login-form"><!--login form-->
				
						<h2>영화 리뷰 감정 평가 프로그램</h2>
						<form id="Form1" name=form1 method="get" onsubmit="return fn_movieSeacrh(); ">
							<input type="text" size="10" maxlength="15" name="movieTitle" placeholder="평점이 궁금한 영화를 검색하세요." />
							<input type="submit" class="btn btn-default" value="검색" onclick="submit">
						</form>
					</div><!--/login form-->
				
			</div>
		</div>
	</section><!--/form-->
	<section id="slider"><!--slider-->
		<div class="container">
			<div class="row">
				<div class="col-sm-12">
					<div id="slider-carousel" class="carousel slide" data-ride="carousel">
						<ol class="carousel-indicators">
							<li data-target="#slider-carousel" data-slide-to="0" class="active"></li>
							<li data-target="#slider-carousel" data-slide-to="1"></li>
							</ol>
						
						<div class="carousel-inner">
							<div class="item active">
								<div class="col-sm-6">
									<h1><span>최다</span>  평점</h1>
									<h2>겨 울 왕 국</h2>
									<p>나는 개인적으로 2편이 더 좋았음. 더 깊어진 스토리에 아름다워진 영상미. 한번 더 볼 의향 있음.</p>
									<p>렛잇고가 대박쳐서 그런지 이번에 노래가 과하게 많다.</p>
									<p>엘사가 성장한  모습으로 행복한 길을선택한것 같아 너무 감동이었음ㅠㅠ진짜 너무 재밌다</p>
									<p>스케일이 더 커지고 뮤지컬보는 기분이었슴다</p>
									<p>1의 재미를  쫓지 못한듯기대가 커서 그런지 밍숭한 맛이였네요스토리도 그냥 저냥...그래픽만은 최고였습니다</p>
									<p>바다에서 말조련하는장면이 압권입니다</p>
									<p>겨울왕국 역시는 역시였다. OST도 1편만큼이나 중독성있다고 생각함ㅋㅋㅋ1편만큼 존잼임</p>		
								</div>
								<div class="col-sm-6">
									<img src="main1.jpg" class="girl img-responsive" alt="" />
									</div>
							</div>
							<div class="item">
								<div class="col-sm-6">
									<h1><span>최고</span>  평점</h1>
									<h2>블 랙 머 니</h2>
									<p>조진웅 배우와 이하늬 배우의 연기 인상깊었습니다.이 사건이 아직 끝나지 않았다는 사실에 놀랐고무지했다는 생각에 부끄러웠네요.</p>
									<p>현재를 살아가는 우리에게 꼭 필요한 영화. 배우들의 연기도 좋았고 마지막 OST 특히 좋았다ㅠㅠ</p>
									<p>금융권 이야기라 어려울 줄 알았는데 편하게 이해하며 영화 즐겼어요! 믿고보는 이하늬 작품!!</p>
									<p>국가부도의 날이후 한국 금융은 어떻게 흘러가는가에대한 생각을 갖고보면 좋을 영화였습니다!</p>
									<p>론스타 사건. 아직도 진행중이라는 사실</p>
									<p>한사람 한사람의 목소리가 모여 거대한 외침을 만드는 영화무거울줄 알았으나 전혀 무겁지 않고 오히려 뿌린 떡밥 걷는 재미가 있다</p>
							
								</div>
								<div class="col-sm-6">
									<img src="main2.jpg" class="girl img-responsive" alt="" />
									</div>
							</div>
							
						</div>
						
						<a href="#slider-carousel" class="left control-carousel hidden-xs" data-slide="prev">
							<i class="fa fa-angle-left"></i>
						</a>
						<a href="#slider-carousel" class="right control-carousel hidden-xs" data-slide="next">
							<i class="fa fa-angle-right"></i>
						</a>
					</div>
					
				</div>
			</div>
			
		</div>
	</section><!--/slider-->
	
  
    <script src="js/jquery.js"></script>
	<script src="js/price-range.js"></script>
    <script src="js/jquery.scrollUp.min.js"></script>
	<script src="js/bootstrap.min.js"></script>
    <script src="js/jquery.prettyPhoto.js"></script>
    <script src="js/main.js"></script>
    
    <script>
    	var fn_movieSeacrh = function(){
    		$.ajax({
				type:'get',
				data:$("#Form1").serialize(),
				dataType:'json',
				url:'http://localhost:8082/py_getMovieCrawl.py',
				async:true,	// false 동기
				beforeSend:function(xhr){/*Screen.showFilm();*/},
				error:function(xhr,status,error){/*Screen.hideFilm();*/},
				complete:function(xhr,status){/*Screen.hideFilm();*/},
				success:function(data){
					console.log(data);
				}
    		});
    		
    		
    		return false;
    	}
    </script>
</body>
</html>