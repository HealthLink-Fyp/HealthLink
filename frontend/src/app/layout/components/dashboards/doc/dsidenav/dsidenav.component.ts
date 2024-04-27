import { Component, OnInit } from '@angular/core';
import { DoctorService } from 'src/app/services/doctor/doctor.service';

@Component({
  selector: 'app-dsidenav',
  templateUrl: './dsidenav.component.html',
  styleUrls: ['./dsidenav.component.css']
})
export class DsidenavComponent implements OnInit {

  doctorData:any={};

  constructor(private doctorService:DoctorService){}
  
  ngOnInit(): void {
    this.doctorService.getDoctor().subscribe((res: any) => {
      this.doctorData = res;
      console.log("coming from dashboard", this.doctorData);
    });
  }

}
