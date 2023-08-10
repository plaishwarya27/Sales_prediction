import { Component, OnInit, AfterViewInit } from '@angular/core';
import { Router } from '@angular/router';
import { Chart, registerables } from 'chart.js';
import { HttpClient } from '@angular/common/http';
import { AuthService } from '../auth.service';

@Component({
  selector: 'app-chart',
  templateUrl: './chart.component.html',
  styleUrls: ['./chart.component.css']
})
export class ChartComponent implements OnInit {

  dates: any = [];
  salesValue: any = [];
  forecastValue: any = [];
  list: any = [];
  chart: any;
  showChart: boolean = false;

  constructor(private http: HttpClient, private route: Router, private authService: AuthService) { Chart.register(...registerables) }

  ngOnInit(): void {
    this.http.get<any>("http://localhost:5000/api/get_Image").subscribe((data) => {
      this.list = data;
      //console.log(this.tempList['date'])
      for (let i = 0; i < this.list['sales'].length; i++) {
        let t1 = this.list['date'][i]
        //console.log(t1)
        let t2 = Number(this.list['sales'][i])
        //console.log(t2)
        let cord = {
          x: t1, y: t2
        }
        this.dates.push(t1);
        this.salesValue.push(cord);
      }
      for (let i = 0; i < this.list['forecast'].length; i++) {
        let t1 = this.list['date'][this.list['fromD'] + i]
        console.log(t1)
        let t2 = Number(this.list['forecast'][i])
        console.log(t2)
        let cord = {
          x: t1, y: t2
        }
        //this.dates.push(t1);
        this.forecastValue.push(cord);
      }
      console.log(this.forecastValue);

    });
  }

  get_data() {
    this.showChart = true;
    const h = new Chart('lineChart', {
      type: 'line',
      data: {
        labels: this.dates,
        datasets: [{
          label: 'Sales',
          data: this.salesValue,
          tension: 0.3,
          borderColor: 'rgba(92, 154, 247)',
          backgroundColor: 'rgba(92, 154, 247)'
        },
        {
          label: 'Forecast',
          data: this.forecastValue,
          tension: 0.3,
          borderColor: 'rgba(242, 120, 63)',
          backgroundColor: 'rgba(242, 120, 63)'
        }]
      },
      options: {
        scales: {

        }
      }
    });
  }
  logOut(): void {
    this.authService.logOut(); {
      this.authService.logOut(); { }
    }
  }
}
