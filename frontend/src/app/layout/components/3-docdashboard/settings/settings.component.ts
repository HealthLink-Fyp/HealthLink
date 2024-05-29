import { Component } from '@angular/core';
import { Route, Router } from '@angular/router';
import { DoctorService } from 'src/app/architecture/services/doctor/doctor.service';
import { Location } from '@angular/common';

@Component({
  selector: 'app-settings',
  templateUrl: './settings.component.html',
  styleUrls: ['./settings.component.css']
})
export class SettingsComponent {

  constructor(private doctorService:DoctorService,private router:Router, private location: Location){}

  goBack(): void {
    this.location.back();
  }


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
