import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { DoctorService } from 'src/app/architecture/services/doctor/doctor.service';
import { PatientService } from 'src/app/architecture/services/patient/patient.service';

@Component({
  selector: 'app-about',
  templateUrl: './about.component.html',
  styleUrls: ['./about.component.css']
})
export class AboutComponent {
  doctorBioData:any={};

  constructor(private patientService:PatientService,private route:ActivatedRoute){}
  
  key:any=''

  ngOnInit(): void {
   this.key=this.route.snapshot.paramMap.get('doctorId');
    
    this.patientService.getDoctorProfile(this.key).subscribe(
      (res:any)=>{
        this.doctorBioData=res;
        console.log("i am doctor profile data for patient : ",this.doctorBioData);
      }
    )
  }

}
