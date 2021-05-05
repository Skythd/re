from System.Net import WebClient, HttpWebRequest, WebRequest
from System.Text import Encoding
from System.IO import StreamReader, StreamWriter, MemoryStream, SeekOrigin, Directory, Path


##########################################################
###         User Fills Out These Variables             ###
###       hyperLink and imageURL are optional          ###
##########################################################
webHookURL = "https://discordapp.com/api/webhooks/willbeareallylongjumbleofnumbersnadlettershere"
message = "Hello from in UO!!"
hyperLink = ""
imageURL = "https://i1.sndcdn.com/artworks-000505122936-p04hws-t500x500.jpg"
##########################################################
###         Don't Change Settings Below Here           ###
##########################################################
#sending data via AJAX
data = (webHookURL + "`" + message + "`" + hyperLink + "`" + imageURL)        
URI = 'https://www.unnaturalnature.com/uothief/REWebHook/'
PARAMETERS = "sending=" + data
request = WebRequest.Create(URI)
request.ContentType = "application/x-www-form-urlencoded"
request.Method = "POST"
bytes = Encoding.ASCII.GetBytes(PARAMETERS)
request.ContentLength = bytes.Length
reqStream = request.GetRequestStream()
reqStream.Write(bytes, 0, bytes.Length)
reqStream.Close()
response = request.GetResponse()
result = StreamReader(response.GetResponseStream()).ReadToEnd()
Misc.SendMessage("Response: {}".format(result))