from requests_html import HTMLSession
session = HTMLSession()

#x = "https://www.maxim.com/.image/t_share/MTUzMjI4NjU2MzY0MjM0MzYw/martin.png"
x = "https://instagram.fcgk6-1.fna.fbcdn.net/vp/bf1baec5216107840d1a55b0c20e44e7/5D1D6756/t51.2885-15/sh0.08/e35/s640x640/51346029_2234231520149381_5091595914720554950_n.jpg?_nc_ht=instagram.fcgk6-1.fna.fbcdn.net"

getf = session.get(x)
print(getf.content)
with open("foto_test2.jpeg", 'wb') as file:
    file.write(getf.content)