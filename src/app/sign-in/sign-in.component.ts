import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService, ResponseObject } from '../auth.service';

@Component({
  selector: 'app-sign-in',
  templateUrl: './sign-in.component.html',
  styleUrls: ['./sign-in.component.css']
})
export class SignInComponent implements OnInit {
  form: any = {
    username: null,
    password: null
  };
  status: any;
  response: ResponseObject | undefined;
  isLoggedIn = false;
  isLoginFailed = false;
  errorMessage = '';
  constructor(private authService: AuthService, private route: Router) { }

  ngOnInit(): void {
  }
  onSubmit(): any {
    console.log("Printed");
    const { username, password } = this.form;
    console.log(username);
    this.authService.login(username, password).subscribe(
      (data: ResponseObject) => {
        this.response = { ...data }
        this.isLoggedIn = this.response['data']
        this.status = this.response['status']
        if (this.status != 200) {
          alert(this.status)
        }
        if (this.isLoggedIn) {
          this.authService.token = this.response['token'];
          localStorage.setItem('token', this.authService.token);
          localStorage.setItem('loggedIn', "true");
          this.route.navigate(['../file-upload']);
        }
      },
      err => {
        this.errorMessage = err.error.errorMessage;
        this.isLoginFailed = true;
      }
    ); { }
  }
   logOut(): void {
    this.authService.logOut(); { }
  }
}