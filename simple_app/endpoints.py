from asyncio.windows_events import NULL
from importlib.resources import path
from re import L
# import jwt
from flask_pymongo import pymongo
from flask import jsonify, request
from simple_app.mlSARIMAXMod import *
from simple_app.Final_madhan import *
from datetime import datetime, timedelta
import cv2 as cv
import os as os

con_string = "mongodb+srv://Maddy2k01:shopans2008@cluster0.kwfxwdg.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(con_string)

db = client.get_database('madhanDB')

user_collection = pymongo.collection.Collection(db, 'madhan')
print("MongoDB connected Successfully")

myJWTSecretKey="Madhan"
file=""
plots=""
isLoggedIn=False
userName=""
l=[]
def project_api_routes(endpoints):
    
    #Route For SignUp Form
    @endpoints.route('/get_Details/SignUp', methods=['POST'])
    def get_Details():
        resp = {}
        try:
            req_body = request.json
            user_collection.insert_one(req_body)            
            print("User Data Stored Successfully in the Database.")
            status = "200"
        except Exception as e:
            print(e)
            status = str(e)
        resp["status"] =status
        return resp
    
    #Route For File Uploading And Model Functioning
    @endpoints.route('/file_upload',methods=['POST','GET'])
    def file_upload():
        resp = {}
        global plots
        try:
            file = request.files.get('file')
            fromDate=request.args.get('fromDate')
            toDate=request.args.get('toDate')
            p=str(file.filename)
            plots=p[:len(p)-4]
            randomForestRegressor(file,plots+".png",fromDate,toDate)
            print("Done4")
            global l
            #l=worker_code(file,plots+".png",fromDate,toDate)
            forRegressor()
            print("Done5")
            resp['data']="1"
            #resp['data']="2"
            resp['status']="200"
        except Exception as e:
            print(e)
            print("Inga varthu da")
            resp["status"] =str(e)
        return resp

    #Route for Sending the name of the image
    @endpoints.route('/get_Image',methods=['GET'])
    def get_Image():
        resp={}
        global plots
        global l
        try:
            path=plots+".png"
            status="200"
        except Exception as e:
            print(e)
            status=str(e)
        resp={
            "path":path,
            "date":l[2],
            "forecast":l[1],
            "sales":l[0],
            "fromD":l[3],
            "status":status
        }
        return resp

    #Route SignIn And Login Verification[Uses JWT]
    @endpoints.route('/verify_login/login',methods=['GET','POST'])
    def verify_login():
        resp={}
        global isLoggedIn
        global userName
        try:
            userName=request.args.get('username')
            password=request.args.get('password')
            out=user_collection.find_one({"userName":userName})
            u1=out.get('userName')
            p1=out.get('password')
            #print("**",u1," ",p1)            
            resp['status']="200"
        #     if(userName==u1 and password==p1):
        #         isLoggedIn=True
        #         token = jwt.encode({
        #         'userName': u1,
        #         'exp' : datetime.utcnow() + timedelta(minutes = 60)
        #         },myJWTSecretKey)
        #         resp['token']=token
        #     elif(password!=p1):
        #         raise Exception("Wrong Password")
        #     resp['data']=isLoggedIn
        except Exception as e:
            print(e)
            status={
                "statusCode":"400",
                "statusMessage":str(e)
            }
            if(str(e)=="'NoneType' object has no attribute 'get'"):
                resp["status"]="Not Valid User!"
            else:
                resp["status"]=str(e)
        return resp

    #Route for Profile Verification
    @endpoints.route('/checkStatus',methods=['GET'])
    def checkStatus():
        resp={}
        try:
            # token=request.args.get('token')
            # print(token)
            # isValid=verify_jwt(token)
            users=user_collection.find_one({"userName":userName})
            u1=users.get('userName')
            e1=users.get('emailID')
            resp['data']=isLoggedIn
            resp['Name']=u1
            resp['Email']=e1
            # if(isValid==False):
            #     raise Exception("Not Logged In!")
            resp['status']="200"
        except Exception as e:
            resp['data']=isLoggedIn
            resp['Name']=""
            resp['Email']=""
            resp['status']=str(e)
        return resp

    return endpoints

# #JWT Working Code
# def verify_jwt(token):
#     try:
#         print(token)
#         if(token==NULL):
#             raise Exception("Token Not Found")
#         data = jwt.decode(token, myJWTSecretKey,algorithms=['HS256'])
#         print(data)
#         return True
#     except Exception as e:
#         print(e)
#         return False

def forRegressor():
    img=cv.imread(plots+".png")
    img2=cv.imread('out1.png')
    img3=cv.imread('barForest.png')
    img4=cv.imread('pieForest.png')
    path=r"C:\Users\User\Desktop\angular\try\src\assets"
    (cv.imwrite(os.path.join(path,plots+".png"),img))
    (cv.imwrite(os.path.join(path,"out1.png"),img2))
    (cv.imwrite(os.path.join(path,"barForest.png"),img3))
    (cv.imwrite(os.path.join(path,"pieForest.png"),img4))