import requests

resp=requests.post("http://localhost:5000",
                    files={"file": open('C:\\Python\project\olahcitra\ws.jpg','rb')})
                    
         
print(resp.json())