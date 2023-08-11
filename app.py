from flask import Flask,request,render_template,jsonify
import json


obj=Flask(__name__)

@obj.route('/')
def welcome():
    return "welcome to Flask"

@obj.route('/cal',methods=["GET"])
def math_operation():
    operation=request.json["operation"]
    number1=request.json["number1"]
    number2=request.json["number2"]

    if operation=="add":
        result= int(number1)+int(number2)
    elif operation=="multiply":
        result= int(number1)*int(number2)
    elif operation=="divison":
        result= int(number1)/int(number2)
    else:
        result= int(number1)-int(number2)
    return jsonify(result)

print(__name__)

if __name__ == '__main__':
    obj.run()