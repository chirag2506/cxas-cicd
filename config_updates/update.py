import os

print("hi")
print(os.environ.get("CONFIG_VALUE"))
print(type(os.environ.get("CONFIG_VALUE")))
print(os.environ.get("TARGET_DIR"))
print(type(os.environ.get("TARGET_DIR")))
print("*"*100)