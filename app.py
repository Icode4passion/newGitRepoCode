
print("Hello World")

list=[1,2,3]
for i in list:
    print(i)


from flask import Flask 
app=Flask(__new__)
@app.route("/")
def index():
    return "Hello World"
if __name__ == "__main__":
    app.run(debug=True)


import sqlite3

class newA:
    pass
