import requests

INPUT = "你看fdspa83fds 0[ok [p]]]]fk  fkd[soak[2fo[djsa  of[dsak[ ok1[dsafads "
headers = {
    "Content-Type": "application/json",
}
output = requests.post(
    "http://localhost:5000/text_ask", json={"input": INPUT}, headers=headers
)

print(output.json())

print(123)

print(123)
print(23132)
print(3840138041)
