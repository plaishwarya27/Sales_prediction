import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService, ResponseObject3 } from '../auth.service';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent implements OnInit {
  isHidden: boolean = false;
  response: ResponseObject3 | undefined
  userName!: string;
  emailID!: string;
  constructor(private authService: AuthService, private route: Router) { }

  ngOnInit(): void {
  }
  checkStatus(): void {
    this.authService.checkStatus().subscribe(
      (data: ResponseObject3) => {
        this.response = { ...data }
        this.isHidden = this.response['data']
        console.log(this.response['status'])
        console.log(this.isHidden)
        if (this.response['status'] != "200") {
          alert("Login To See Profile!")
        }
        else {
          localStorage.setItem('LoggedIn', 'true');
        }
        this.userName = this.response['Name']
        this.emailID = this.response['Email']
      },
    )
  }
  logOut(): void {
    this.authService.logOut(); {
      this.authService.logOut(); { }
    }
  }
}
