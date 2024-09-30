$ip = "KALIVMIP"
$port = 9999
$message = "hello from windows!"

$client = new-object System.Net.Sockets.TcpClient($ip,$port)

$stream = $client.getstream()
$writer = New-Object system.io.streamwriter($stream)
$writer.writeline($message)
$writer.flush()

$reader= new-object system.io.streamreader($stream)
$response = $reader.readline()
write-output "Received: $response"