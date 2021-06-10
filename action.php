<?php

//action.php

$connect = new PDO("mysql:host=localhost; dbname=intuitivetarefas", "root", "");

$received_data = json_decode(file_get_contents("php://input"));

$data = array();

if($received_data->query != '')
{
	$query = "
	SELECT * FROM cadop2
	         
							
	WHERE Registro_ANS LIKE '%".$received_data->query."%' OR CNPJ LIKE '%".$received_data->query."%'  OR Representante LIKE '%".$received_data->query."%'OR Razão_Social LIKE '%".$received_data->query."%'
	
	
	";
}
else
{
	$query = "
	SELECT * FROM cadop2
	
	";
}

$statement = $connect->prepare($query);

$statement->execute();

while($row = $statement->fetch(PDO::FETCH_ASSOC))
{
	$data[] = $row;
}

echo json_encode($data);

?>