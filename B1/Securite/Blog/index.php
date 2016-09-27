<html>
	<head>
		<title></title>
	</head>
	<body>
	<?php
		
		$bdd = mysql_connect();

		$connect=mysql_connect('localhost','root','root');
		mysql_select_db('blog',$connect);

		##Get all articles 


		#Si la demande concerne la lecture des articles on inclus la page lire.php
		if(isset($_GET['read'])){
			include($_GET['read'].".php");
		}

		else{
			$query = sprintf("SELECT id,titre,auteur,contenu FROM articles LIMIT 3");
			$result = mysql_query($query);

			$num=mysql_num_rows($result);

			$i=0;

			while($i<$num){
				$titre = mysql_result($result,$i,"titre");
				$auteur = mysql_result($result,$i, "auteur");
				$id = mysql_result($result,$i,"id");
				$contenu = mysql_result($result,$i,"contenu");

				?>
					<div class="row">
						<div class="col-md-6 col-md-offset-3">
							<div class="panel panel-primary">
								<div class="panel-heading">
									<h3 class="panel-title"><a href="index.php?read=lire&article=<?php echo $id; ?>"><?php echo $titre; ?></a></h3>
								</div>
								<div class="panel-body">
									<p><?php echo $contenu; ?></p>
								</div>
								<div class="panel-footer">
									<i><?php echo $auteur; ?></i>
								</div>
							</div>
						</div>
					</div>

				<?php
				$i++;
			}

		}

	?>


	</body>
</html>