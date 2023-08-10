import { Component, OnInit } from '@angular/core';
import { AuthService, ResponseObject2, RObject } from '../auth.service';
import { DomSanitizer, SafeResourceUrl, SafeHtml } from '@angular/platform-browser';
import { Router } from '@angular/router';

@Component({
  selector: 'app-file-upload',
  templateUrl: './file-upload.component.html',
  styleUrls: ['./file-upload.component.css']
})
export class FileUploadComponent implements OnInit {
  file:File|undefined;
  response: ResponseObject2 | undefined;
  hideButton1:boolean=false;
  hideButton2:boolean=false;
  res: RObject | undefined;
  img!: string;
  liimg!: string;
  final!: string;
  fromDate!: string;
  toDate!: string;
  isHidden: boolean = false;
  isLoggedIn: boolean = false;
  public show: SafeResourceUrl | undefined;
  constructor(private authService: AuthService, private sanitizer: DomSanitizer, private route: Router) { }

  ngOnInit(): void {
  }

  onFilechange(event: any) {
    console.log(event.target.files[0])
    this.file = event.target.files[0]
  }
  upload(): void {
    if (this.file) {
      this.authService.uploadfile(this.file, this.fromDate, this.toDate).subscribe(
        (data: RObject) => {
          this.res = { ...data }
          if (this.res['data'] == "1") {
            this.hideButton1 = true;
          }
          if (this.res['data'] == "2") {
            this.hideButton2 = true;
          }
          if (this.res['status'] == "200") {
            alert("File Uploaded!")
          }
          else {
            console.log(this.res['status'])
          }
        }); { }
    }
    else {
      alert("Please select a file first")
    }
  }

  getImage(): any {
    /*this.authService.getImage().subscribe(
      (data: ResponseObject2) => {
        this.isHidden = true;
        this.response = { ...data }
        this.img = this.response['data1']
        console.log(this.img)
      }
    )*/
    this.route.navigate(['../chart'])
  }
  showImage(): any {
    this.route.navigate(['../dashboard'])
  }
  logOut(): void {
    this.authService.logOut(); {
      this.authService.logOut(); { }
    }
  }
}
