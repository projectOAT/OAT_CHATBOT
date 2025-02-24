<?php
header("Access-Control-Allow-Origin: *");
header("Content-Type: application/json");

$data = json_decode(file_get_contents("php://input"), true);
$user_message = $data["message"] ?? "";

$url = "http://localhost:5055/webhook"; // Local Rasa Server URL

$options = [
    "http" => [
        "header"  => "Content-Type: application/json",
        "method"  => "POST",
        "content" => json_encode(["sender" => "user", "message" => $user_message]),
    ],
];

$context  = stream_context_create($options);
$result = file_get_contents($url, false, $context);

echo $result;
?>
