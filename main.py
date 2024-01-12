from flask import Flask,render_template
import requests 

# def randomuser(gender:str,n:int):
#     url="https://randomuser.me/api/"
#     paylaod={
#         "gender":gender,
#         "results": n
#     }
#     response=requests.get(url=url,params=paylaod)
#     return response.json()["results"]
# print(randomuser("male",30))

app=Flask(__name__)

@app.route("/<gender>/<int:n>")
def randomuser(gender,n:int):
    url="https://randomuser.me/api/"  
    paylaod={
        "gender":gender,
        "results":n
    } 
    response=requests.get(url=url,params=paylaod)
    users=[]
    for user in response.json()["results"]:
        users.append(user['name']['first'])
    return render_template("index.html",context={"users":users, "n":n})

if __name__ == '__main__':
    app.run(debug=True)