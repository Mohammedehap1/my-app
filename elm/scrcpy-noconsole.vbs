strCommand = "cmd /c scrcpy.exe -f --no-audio " '--no-audio'

For Each Arg In WScript.Arguments
    strCommand = strCommand & " """ & replace(Arg, """", """""""""") & """"
Next

CreateObject("Wscript.Shell").Run strCommand, 0, false
