from urllib.parse import quote_plus , quote , urlencode

import requests
import json

url_template = "https://aj9dszm84j.execute-api.us-east-2.amazonaws.com/Dev/execution"
value = {
    "output":"{\"Status\":\"Approved\"}",
    "taskToken":"AAAAKgAAAAIABBBBBBBBBBBBBBBBBB#####################WWWWWWWWWWWWWBBBBBBBBBBBBBBBBBBBBBAAAcTqJe5rquzbM38VQh66x2Ug69ZxNcEVfBqwAdlHPhylVim3q17RB8v188xmBjStjMF0ZEXG43999rxLF+qxZDWBxo46deaPL9FtV00GD0fuiw95SEGz85XMaCUGOG0FLVeat7kH8Kib1ZPy2OlST2meYiBD75KphbBc9nbX+dmlwOHeh0GT4NGg7yUGK7HGUrwOjb0b1lDaXuloqrTE7oU8HAYiU13aPClk0M7MmPoD/lgF0luzOcVQdVxW2rk6n0DEjNrxqgwOy8Z+s5bRHjQ5NKS01UbIEAE30s+qmyOOZm/6mpZUB7S2YWlfFqcd9oEvfpW4HbFfe95d1kTp3Cu0X9fE3cT9cOhbhVWRI50L6u4Ur+0qXYaEPHQGJUQ4uh5IEcXKSbdrwIRiG7b3Rns9xFbJrkFcTRgYiqHuCYqsy9DBYwVaeRrYIyBhE/RkE/ozTJTHiaigLz/UqDub7Hxlx12vELrC++lIZmtP32kJy0pIJ1D0z6YTzIGXO/DcmGIq7IIFANHyF3YUp6qmijAV2RCcF/HDR3XU9QYq4ytL42iElG9JIas1+eIjPwv5qG0cJhd9gPi8InwBNKdoDCL2ukjs1GhaC/NmfIGanFTd"
}


data={
    'output':{'Status':'Approved'},
    'taskToken':"BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB@@@@@@@22222BB##################/fxeuaGK8dIhN62Wt7B5ZT82qxGa1b2KlOS2h+4HaWSUhuqeneoJZiREDGiav39rOjePFkotJjgrnC6VSP3BGlAXjZGR0rkwyDslQUmC+htu2y49wAPEF26NII4+dv/YoDZ94gKiISw+INGwpd7oFu5leXN5/t65rv1DlaTEw61uUghF6vWYjQ7ting9zKhPJTmVOEwCAAw2ieqpq00O47q4AF5l/mYHO4NrcVoDPvtRnsKl/i5TaTbWY63O3ygq3xJda8bJbD1zsTFkCIiBP5sORu1ViRd6hR/BEYljmH6NTBkWtgBXH2dxeAQRFarSFeOGQGB0E2i3Yyvw9sAbcbHtU1VtWLgWHQzyZ7WZxwSH9VVrmksXi/SutwrLfAVqZmkSvXZKj7VjauYrX6Cx1p22bZupUjCqYjK39fswE8B+CY7ogiSGIrdYuh0LDzjrYMjgSiDSNbyLlFeQnMRwMTXcULeTPp+viocabAKc/fwSVui7gHMUCrVAYg0ZG5V5MiLakVO3rO5qvbvBd/s0KLZpJgW98Y3zCjDuubSRehifmW13ZLN8otq0YovvjDKf6U6e4FIQKFnLL97lWm5pXa9i9urIP/SLN0HXlQ"
}

# value = json.dumps(data)
# print(value)
headers = {'Content-type': 'application/json'}
response = requests.post(url_template, json = value,headers=headers)
print(response.json())