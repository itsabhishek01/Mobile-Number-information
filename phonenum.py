import phonenumbers
from phonenumbers import carrier,geocoder,timezone
from phonenumbers.phonenumberutil import _MOBILE_TOKEN_MAPPINGS
mobnum=input("Enter The 10 Digit Mobile Number with Country Code: ")
mobnum=phonenumbers.parse(mobnum)

print(timezone.time_zones_for_number(mobnum))
print(carrier.name_for_number(mobnum,"en"))
print(geocoder.description_for_number(mobnum,"en"))

print("valid mobile number: ",phonenumbers.is_valid_number(mobnum))
print("Checking possibility of number",phonenumbers.is_possible_number(mobnum))
