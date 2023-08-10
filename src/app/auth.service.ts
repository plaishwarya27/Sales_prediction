import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Token } from '@angular/compiler';
const urlS = "http://localhost:5000/api/get_Details/";
const httpOptions = {
  headers: new HttpHeaders({ 'Content-Type': 'application/json' })
};
export interface ResponseObject {
  data: boolean;
  status: any;
  token: string;
}
export interface ResponseObject2 {
  data1: string;
}
export interface ResponseObject3 {
  data: boolean;
  Name: string;
  Email: string;
  status: any;
}
export interface RObject {
  data:string;
  status: any;
}
@Injectable({
  providedIn: 'root'
})
export class AuthService {
  loggedIn = localStorage.getItem('loggedIn');
  token = localStorage.getItem("token");
  constructor(private http: HttpClient) { }
  register(userName: string, emailID: string, password: string): Observable<any> {
    return this.http.post(urlS + "SignUp", {
      userName,
      emailID,
      password
    }, httpOptions);
  }
  login(username: string, password: string): Observable<any> {
    let urlL = 'http://localhost:5000/api/verify_login/' + 'login?username=' + username + '&password=' + password;
    return this.http.get<ResponseObject>(urlL);
  }
  uploadfile(file: File, fromDate: string, toDate: string) {
    let formd = new FormData();
    formd.append('file', file);
    let urlF = 'http://localhost:5000/api/file_upload?file=' + formd + '&fromDate=' + fromDate + '&toDate=' + toDate;
    return this.http.post<RObject>(urlF, formd);
  }
  //getImage(): Observable<any> {
  //  return this.http.get<ResponseObject2>('http://localhost:5000/api/get_Image');
  //}
  checkStatus(): Observable<any> {
    return this.http.get<ResponseObject3>('http://localhost:5000/api/checkStatus?token=' + this.token);
  }
  logOut() {
    this.token = "";
    console.log("Logging Out");
    localStorage.removeItem('token');
    localStorage.removeItem('loggedIn')
  }
}
