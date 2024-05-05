import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { PatientService } from 'src/app/architecture/services/patient/patient.service';

@Component({
  selector: 'app-settings',
  templateUrl: './settings.component.html',
  styleUrls: ['./settings.component.css']
})
export class SettingsComponent {

  constructor(private patientService:PatientService,private router:Router){}


  updatePatientForm()
    {
      this.router.navigate(['/patient/form'],{queryParams:{updateMode:true}});
    }

    updatePatientProfile()
    {
      this.router.navigate(['/patient/Sign-up'],{queryParams:{updateMode:true}});
    }


    onDeletePatient()
    {
      this.patientService.deletePatient().subscribe(
        (reponse:any)=>{
          console.log("patient deleted successfully",reponse)
        }
      )
    }
  
    onDeletePatientForm()
    {
      this.patientService.delPatForm().subscribe(
        (response:any)=>{
          console.log("paitent form deleted successfully",response);
        }
      )
    }

}
