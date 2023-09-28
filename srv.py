import os

print(os.getcwd())


data = {"key": "val"}


print(data)

tml = "info : {}"

print(tml.format(data))

tml = "info : {key}"

print(tml.format(**data))


print(tml.format(key = data["key"]))
