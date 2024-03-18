import { Component, OnInit } from '@angular/core';
import { DoctorService } from 'src/app/services/doctor/doctor.service';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit{

  constructor(private doctorService:DoctorService){}

  doctorData:any={};

  ngOnInit(): void {
    this.doctorService.getDoctor().subscribe((res:any)=>{
        this.doctorData=res;
        console.log("saved in doctor dashboard",this.doctorData)
    })
  }

 

}
