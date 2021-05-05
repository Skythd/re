<?php
$data = $_POST['sending'];
$data = explode("`", $data);
$wURL = $data[0];
$mess = $data[1];
$link = $data[2];
$imgL = $data[3];

if($wURL !=""){
try{
$webhookurl = $wURL;
$timestamp = date("c", strtotime("now"));
$json_data = json_encode([
	"content" => '',
    // Username
    "username" => "razorenhanced.net",
    "avatar_url" => "http://razorenhanced.net/img/razor-enhanced-splash.png",
    // Text-to-speech
    "tts" => false,
    // Embeds Array
    "embeds" => [
        [
            // Embed Title
            "title" => "User Message via razorenhanced.net",
            // Embed Type
            "type" => "rich",
            // Embed Description
            "description" => $mess,
            // URL of title link
            "url" => $link,
            // Timestamp of embed must be formatted as ISO8601
            "timestamp" => $timestamp,
            // Embed left border color in HEX
            "color" => hexdec( "FF0000" ),
            // Footer
            "footer" => [
                "text" => "http://razorenhanced.net/",
                "icon_url" => ""
            ],
            // Image to send
            "image" => [
                "url" => $imgL
            ]
        ]
    ]
], JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE );



$ch = curl_init( $webhookurl );
curl_setopt( $ch, CURLOPT_HTTPHEADER, array('Content-type: application/json'));
curl_setopt( $ch, CURLOPT_POST, 1);
curl_setopt( $ch, CURLOPT_POSTFIELDS, $json_data);
curl_setopt( $ch, CURLOPT_FOLLOWLOCATION, 1);
curl_setopt( $ch, CURLOPT_HEADER, 0);
curl_setopt( $ch, CURLOPT_RETURNTRANSFER, 1);

$response = curl_exec( $ch );
// If you need to debug, or find out why you can't send message uncomment line below, and execute script.
//echo $response;
echo "Message Sent";
curl_close( $ch );
}
catch(exception $e){
echo $e;
}
finally{
die();
}
}
?>