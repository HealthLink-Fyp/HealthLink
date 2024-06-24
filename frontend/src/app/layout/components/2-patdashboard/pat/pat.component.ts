import { Component, OnInit } from '@angular/core';
import { PatientService } from 'src/app/architecture/services/patient/patient.service';

@Component({
  selector: 'app-pat',
  templateUrl: './pat.component.html',
  styleUrls: ['./pat.component.css']
})
export class PatComponent implements OnInit {
  patientData: any = {};

  constructor(private patientService:PatientService){}
  
  ngOnInit(): void {
    this.patientService.getPatient().subscribe((res: any) => {
      this.patientData = res;
      // console.log("coming from dashboard", this.patientData);
    });
  }
}