 <?php

$nm = $_POST['name'];
$fb = $_POST['feedback'];

//echo exec("/home/mugunth/anaconda3/bin/python nltk1.py $fb 2>&1");
echo exec("/home/mugunth/anaconda3/bin/python nltk1.py  '$fb'");

$servername = "localhost";
$username = "root";
$password = "spiderman";
$dbname = "feedback";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$sql = mysqli_query($conn,"INSERT INTO original_feedback(name,feedback) VALUES('$nm','$fb')");
$conn->close();

echo("Thank you");

?>
