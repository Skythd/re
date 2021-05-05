

def gettarget():        
    enemy = Target.GetTargetFromList( 'beetle' )
    if enemy != None:
        webhook('found beetle')
        Misc.Pause(1000)
        webhook('@here')
        bluebeetle = Target.GetTargetFromList('bluebeetle')
        if bluebeetle != None:
            webhook('its Blue')
        else:
            webhook('its not blue')



def webhook(msg):
    URI = 'https://discordapp.com/api/webhooks/654131394854781018/KySfeUnLjoFmqfmf154_1V22nxkzGnDmOP6-j8Kj__Ei8boMeHwzir6irC57rIY65_6q'
    alert = msg
    report = "content="+ alert
    PARAMETERS=report
    from System.Net import WebRequest
    request = WebRequest.Create(URI)
    request.ContentType = "application/x-www-form-urlencoded"
    request.Method = "POST"
    from System.Text import Encoding
    bytes = Encoding.ASCII.GetBytes(PARAMETERS)
    request.ContentLength = bytes.Length
    reqStream = request.GetRequestStream()
    reqStream.Write(bytes, 0, bytes.Length)
    reqStream.Close()
    response = request.GetResponse()
    from System.IO import StreamReader
    result = StreamReader(response.GetResponseStream()).ReadToEnd().replace('\r', '\n')

while True:    
    gettarget()
    Misc.Pause(10000)