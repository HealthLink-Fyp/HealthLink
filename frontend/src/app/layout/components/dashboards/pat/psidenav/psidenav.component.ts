

import { Component, OnInit } from '@angular/core';
import { PatientService } from 'src/app/services/patient/patient.service';

@Component({
  selector: 'app-psidenav',
  templateUrl: './psidenav.component.html',
  styleUrls: ['./psidenav.component.css']
})
export class PsidenavComponent implements OnInit {
 

  constructor(private patientser:PatientService){}

  patientData:any={};

ngOnInit(): void {
  this.patientser.getPatient().subscribe((res: any) => {
    this.patientData = res;
    console.log("coming from dashboard", this.patientData);
  });
}

}


