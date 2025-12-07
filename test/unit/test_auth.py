from app.services import SecurityService

password = "billgates1$"

service = SecurityService()

print(service.hash_password(password=password))
