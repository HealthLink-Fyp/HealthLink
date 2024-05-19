import { Component } from '@angular/core';
import { Route, Router } from '@angular/router';
import { DoctorService } from 'src/app/architecture/services/doctor/doctor.service';

@Component({
  selector: 'app-settings',
  templateUrl: './settings.component.html',
  styleUrls: ['./settings.component.css']
})
export class SettingsComponent {

  constructor(private doctorService:DoctorService,private router:Router){}

  updateDoctorForm()
  {
    this.router.navigate(['/doctor/form'],{queryParams:{updateMode:true}});
  }

  updateDoctorProfile()
  {
    this.router.navigate(['/account/Sign-up'],{queryParams:{updateMode:true}});
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
