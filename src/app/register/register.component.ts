import { Component, OnInit } from '@angular/core';
import { AuthService } from '../auth.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {
  form: any = {
    userName: null,
    emailID: null,
    password: null,
    rpassword: null
  };
  isSuccessful = false;
  isSignUpFailed = false;
  errorMessage = '';
  constructor(private authService: AuthService, private route: Router) { }

  ngOnInit(): void {
  }

  onSubmit(): void {
    const { userName, emailID, password, rpassword } = this.form;
    console.log(this.form.password == this.form.rpassword);
    if (this.form.password == this.form.rpassword) {
      this.authService.register(userName, emailID, password).subscribe(
        data => {
          console.log(data);
          this.isSuccessful = true;
          this.isSignUpFailed = false;
        },
        errro1 => {
          this.errorMessage = errro1.error.message;
          this.isSignUpFailed = true;
        }
      );
    }
    else {
      alert("ReType Password Doesn't Match!");
    }
    this.route.navigate(['../sign-in']);
  }
}
