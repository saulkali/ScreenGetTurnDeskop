dim xHttp: Set xHttp = createObject("Microsoft.XMLHTTP")
dim bStrm: Set bStrm = createObject("Adodb.Stream")

dim versionNow: Set versionNow = "1.0.0.0"
dim urlCheckVersion: Set urlCheckVersion = "http://example.com/someimage.json"
dim urlGetZipFile: Set urlGetZipFile = "http://example.com/someimage.zip"
dim pathSaveFile: Set pathSaveFile = "c:\temp\someimage.png"


xHttp.Open "GET",urlCheckVersion,False
xHttp.send
strJson = xHttp.responseText

Set VersionControl = ParseJson(strJson)

If VersionControl.version = versionNow Then
    WScript.Quit 1
Else
    xHttp.Open "GET", urlGetZipFile ,False
    xHttp.Send

    with bStrm
        .type = 1
        .open
        .write xHttp.responseBody
        .savetofile = pathSaveFile,2
    end with