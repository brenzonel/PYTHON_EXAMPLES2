import time
import pyotp
import qrcode

key = "FCFMESGENIAL"
#login 
#select name from user where name = p_name and pwd = p_pwd
#Primero
#Haciendo QR para validacion en APP de Autenticacion
uri = "https://www.facebook.com/recover/code/?ph[0]=%2B**********46&rm=send_sms&hash=AUa1J45G79NQMqzu52A"
#pyotp.totp.TOTP(key).provisioning_uri(name="Brenzon",
#                                            issuer_name="Prueba_FCFM")
print(uri)
qrcode.make(uri).save("TIMEOTP.png")

timeotp = pyotp.TOTP(key)

while True:
    print(timeotp.verify(input("Ingrese Codigo Chido: ")))