from dotenv import dotenv_values

config = dotenv_values("../.env")  # config = {"USER": "foo", "EMAIL": "foo@example.org"}

print(config)  # prints "foo"

print(config["API_astrometry_net"])  # prints "foo"

print(type(config["API_astrometry_net"])) 
