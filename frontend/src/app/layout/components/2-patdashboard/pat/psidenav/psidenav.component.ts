

import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { AuthService } from 'src/app/architecture/services/auth.service';
import { PatientService } from 'src/app/architecture/services/patient/patient.service';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-psidenav',
  templateUrl: './psidenav.component.html',
  styleUrls: ['./psidenav.component.css']
})
export class PsidenavComponent implements OnInit {
 

  
  

  constructor(private patientser:PatientService,private authService:AuthService, private router:Router,private route:ActivatedRoute){}

  patientData:any={};

ngOnInit(): void {
  this.patientser.getPatient().subscribe((res: any) => {
    this.patientData = res;
    console.log("coming from dashboard", this.patientData);
  });
}

logout() {
  this.authService.logout().subscribe(() => {
    this.authService.accessToken = '';
    AuthService.authEmitter.emit(false);
    localStorage.removeItem('token');
  });
}

}


