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
								<li><a href="#"></i> Ŭ���� ��ǻ�� �⸻����</a></li>
								<li><a href="#"></i> ����: ȫ���� ����: ������ , �ڽ���</a></li>
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
				
						<h2>��ȭ ���� ���� �� ���α׷�</h2>
						<form id="Form1" name=form1 method="get" onsubmit="return fn_movieSeacrh(); ">
							<input type="text" size="10" maxlength="15" name="movieTitle" placeholder="������ �ñ��� ��ȭ�� �˻��ϼ���." />
							<input type="submit" class="btn btn-default" value="�˻�" onclick="submit">
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
									<h1><span>�ִ�</span>  ����</h1>
									<h2>�� �� �� ��</h2>
									<p>���� ���������� 2���� �� ������. �� ����� ���丮�� �Ƹ��ٿ��� �����. �ѹ� �� �� ���� ����.</p>
									<p>���հ� ����ļ� �׷��� �̹��� �뷡�� ���ϰ� ����.</p>
									<p>���簡 ������  ������� �ູ�� ���������Ѱ� ���� �ʹ� �����̾����Ф���¥ �ʹ� ��մ�</p>
									<p>�������� �� Ŀ���� �����ú��� ����̾�����</p>
									<p>1�� ��̸�  ���� ���ѵ��밡 Ŀ�� �׷��� �ּ��� ���̿��׿佺�丮�� �׳� ����...�׷��ȸ��� �ְ����ϴ�</p>
									<p>�ٴٿ��� �������ϴ������ �б��Դϴ�</p>
									<p>�ܿ�ձ� ���ô� ���ÿ���. OST�� 1��ŭ�̳� �ߵ����ִٰ� �����Ԥ�����1��ŭ ������</p>		
								</div>
								<div class="col-sm-6">
									<img src="main1.jpg" class="girl img-responsive" alt="" />
									</div>
							</div>
							<div class="item">
								<div class="col-sm-6">
									<h1><span>�ְ�</span>  ����</h1>
									<h2>�� �� �� ��</h2>
									<p>������ ���� ���ϴ� ����� ���� �λ������ϴ�.�� ����� ���� ������ �ʾҴٴ� ��ǿ� ��������ߴٴ� ������ �β������׿�.</p>
									<p>���縦 ��ư��� �츮���� �� �ʿ��� ��ȭ. ������ ���⵵ ���Ұ� ������ OST Ư�� ���Ҵ٤Ф�</p>
									<p>������ �̾߱�� ����� �� �˾Ҵµ� ���ϰ� �����ϸ� ��ȭ �����! �ϰ��� ���ϴ� ��ǰ!!</p>
									<p>�����ε��� ������ �ѱ� ������ ��� �귯���°������� ������ ������ ���� ��ȭ�����ϴ�!</p>
									<p>�н�Ÿ ���. ������ �������̶�� ���</p>
									<p>�ѻ�� �ѻ���� ��Ҹ��� �� �Ŵ��� ��ħ�� ����� ��ȭ���ſ��� �˾����� ���� ������ �ʰ� ������ �Ѹ� ���� �ȴ� ��̰� �ִ�</p>
							
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
				async:true,	// false ����
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