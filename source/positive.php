<html>
<body style="background-color:white"> 

  <?php
  $file="../data/posdata.txt";
  $linecount = 0;
  $handle = fopen($file, "r");
  while(!feof($handle)){
    $line = fgets($handle, 4096);
    $linecount = $linecount + substr_count($line, PHP_EOL);
  }


  //echo $linecount;
  $myfile="../data/posdata.txt";
  $lines=file($myfile);
  echo $lines[1];
  $i=1;
  for($i=0;$i<$linecount;$i++){
    echo $lines[$i];
    echo"<br>";
  }
  fclose($handle);

  ?>
</body>
</html>
