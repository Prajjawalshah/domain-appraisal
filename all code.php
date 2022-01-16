<?php
$servername = "localhost";
$username = "root";
$dbname = "mytest";


// Create connection
$conn = new mysqli($servername, $username,$dbname);

// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

$sql = "CREATE TABLE MyProject(
id INT(6) AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(30),
phone VARCHAR(10),
email VARCHAR(30))";

if ($conn->query($sql) === TRUE) {
  echo "Table MyProject created successfully";
} else {
  echo "Error creating table: " . $conn->error;
}

$conn->close();


//display Data Select
$sql = "SELECT id, name, phone, email FROM MyProject";
$result = $conn->query($sql);

if ($result) {
  // output data of each row
  while($row = $result->fetch_assoc()) {
    echo "id: " . $row["id"]. " - Name: " . $row["name"]. " " . $row["phone"]. " " .$row["email"]."<br>";
  }
} 

//Delete duplicate

$sql = "DELETE t1 FROM MyProject t1, MyProject t2 WHERE t1.id < t2.id AND t1.name = t2.name";

//Load file

$sql = "LOAD DATA INFILE 'C:/Users/LENOVO/Desktop/foo.txt' 
INTO TABLE MyProject COLUMNS TERMINATED BY ',' LINES TERMINATED BY '\r\n'(column name);";
?>