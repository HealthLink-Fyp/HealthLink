import { Component } from '@angular/core';
import { AuthService } from 'src/app/architecture/services/auth.service';
import { PatientService } from 'src/app/architecture/services/patient/patient.service';

@Component({
  selector: 'app-pappointment',
  templateUrl: './pappointment.component.html',
  styleUrls: ['./pappointment.component.css']
})
export class PappointmentComponent {

  constructor(private authService:AuthService, private patientService:PatientService){}

  onupdateAppointment:boolean=false;

  pkAppointment:any='';
  
  bookedAppointments:any[] = []; 

  onbookAppointment:boolean=false;
 
  appointmentData: any = {
    start:'',
    doctor:'',
    patient:'',
    pkAppointment:''
  };

  onAppointment(docId:any)
  {

    this.onbookAppointment=true;
    
    this.authService.user().subscribe((res:any)=>{
      this.appointmentData.patient=res.id;
      console.log("the patient id is : ",res.id)

    
    
    this.appointmentData.doctor=docId;

    this.patientService.makeAppointment(this.appointmentData).subscribe((response:any)=>{
      console.log(response);
    })
  });
  }

  onbookedAppointments()
  {
     this.patientService.getbookedAppointments().subscribe(
      (response:any)=>{
        this.bookedAppointments=response;
      }
     )
  }

  onUpdateAppointment(appointId:any,docId:any) {

    this.onupdateAppointment=true;
    this.appointmentData.doctor=docId;
    this.appointmentData.pkAppointment=appointId;
   
  }

  onSubmitUpdatedAppointment() {
    this.patientService.updateAppointment(this.appointmentData,this.appointmentData.pkAppointment).subscribe((response:any)=>{
      console.log(response);
    })
  }
}

