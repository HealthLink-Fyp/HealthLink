import { DoctorService } from '../../../../architecture/services/doctor/doctor.service';
import { Component, OnInit } from '@angular/core';
import { PatientService } from 'src/app/architecture/services/patient/patient.service';

@Component({
  selector: 'app-doc',
  templateUrl: './doc.component.html',
  styleUrls: ['./doc.component.css']
})
export class DocComponent implements OnInit{
  doctorData:any={};

  constructor(private doctorService:DoctorService){}
  
  ngOnInit(): void {
    this.doctorService.getDoctor().subscribe((res: any) => {
      this.doctorData = res;
      console.log("coming from dashboard", this.doctorData);
    });
  }
}
