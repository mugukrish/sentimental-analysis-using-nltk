<html>
<head>
  <title>All insights</title>
</head>
<?php
echo exec("/home/mugunth/anaconda3/bin/python analy.py 2>&1")
?>
<style>
body{
    position: relative;
    background-image: url("plain.jpg");
    background-repeat:no-repeat;
}
</style>
<body>
<center> <h1>What people think<h1><center>
<img style="padding:30" src="images/pos.png" alt="postitve wordcloud">
<img style="padding:30" src="images/neg.png" alt="negative wordcloud">
<img style="padding:30" src="images/pie.png" alt="pie chart"><br>

<span style="padding:30"><iframe  src="source/positive.php" height="300" width="500"></iframe>
</span>
<span style="padding:30"><iframe  src="source/negative.php" height="300" width="500"></iframe>
</span>

</body>

</html>
