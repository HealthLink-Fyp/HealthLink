import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { DoctorService } from 'src/app/services/doctor/doctor.service';
import { PatientService } from 'src/app/services/patient/patient.service';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit{

  constructor(private doctorService:DoctorService,private patientService:PatientService, private route:ActivatedRoute,private router:Router){}

  doctorData:any={};

  doctorProfileData:any={};

  ngOnInit(): void {

    // when the doctor itself is logged in

    this.doctorService.getDoctor().subscribe((res:any)=>{
        this.doctorData=res;
        console.log("i am a doctor saved in doctor dashboard",this.doctorData)
    })


    // Fetch doctor's data for patient for viewing using the user ID from the route parameter

    const userId=this.route.snapshot.params['userId'];
    
    this.patientService.getDoctorProfile(userId).subscribe(
      (res:any)=>{
        this.doctorProfileData=res;
        console.log("i am doctor profile data for patient : ",this.doctorProfileData);
      }
    )
  }

  updateDoctorForm()
  {
    this.router.navigate(['/doctor'],{queryParams:{updateMode:true}});
  }

  updateDoctorProfile()
  {
    this.router.navigate(['/register'],{queryParams:{updateMode:true}});
  }

  onDeleteDoctor()
  {
    this.doctorService.deleteDoctor().subscribe(
      (reponse:any)=>{
        console.log("doctor deleted successfully",reponse)
      }
    )
  }

  onDeleteDoctorForm()
  {
    this.doctorService.delDocForm().subscribe(
      (response:any)=>{
        console.log("doctor form deleted successfully",response);
      }
    )
  }

}
