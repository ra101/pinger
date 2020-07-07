Set WshShell = CreateObject("WScript.Shell") 
WshShell.Run chr(34) & "python.exe" & Chr(34) &"pinger.py" & Chr(34), 0
Set WshShell = Nothing