import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { AuthService } from 'src/app/architecture/services/auth.service';
import { PatientService } from 'src/app/architecture/services/patient/patient.service';

@Component({
  selector: 'app-pappointment',
  templateUrl: './pappointment.component.html',
  styleUrls: ['./pappointment.component.css']
})
export class PappointmentComponent implements OnInit {

  constructor(private currentPatient:AuthService,private authService:AuthService, private patientService:PatientService, private route:ActivatedRoute, private router:Router){}

  ngOnInit(): void {

    // by clicking book appoointment, get doctor id from docsearch
    this.appointmentData.doctor=this.route.snapshot.paramMap.get('doctorId');

    // get the current logged in patient user id 
    this.currentPatient.user().subscribe((res:any)=>{
           this.appointmentData.patient=res.id;
    })


    this.onbookedAppointments();

  }

  onupdateAppointment:boolean=false;

  pkAppointment:any='';
  
  bookedAppointments:any[] = []; 

  appointmentData: any = {
    start:'',
    doctor:'',
    patient:'',
    pkAppointment:''
  };

  presentAppointments:boolean=false;

 

  onBookAppointment()
  {

    this.patientService.makeAppointment(this.appointmentData).subscribe((response:any)=>{
      console.log(response);
    })
 
  }

  onbookedAppointments() {
    this.patientService.getbookedAppointments().subscribe(
      (response: any) => {
        this.bookedAppointments = response;
        // Add expiresAt property to each appointment
        this.bookedAppointments.forEach((appointment) => {
          appointment.expiresAt = new Date(appointment.start).getTime() + 30 * 60 * 1000; // 30 minutes
          // appointment.expiresAt = new Date(appointment.start).getTime() + 3 * 60 * 1000; // 3 minutes
        });
      }
    );
  }

  onUpdateAppointment(appointId:any,docId:any) {

    this.onupdateAppointment=true;

    this.presentAppointments=false;

    this.appointmentData.doctor=docId;
    this.appointmentData.pkAppointment=appointId;

   
  }

  onSubmitUpdatedAppointment() {
    this.patientService.updateAppointment(this.appointmentData,this.appointmentData.pkAppointment).subscribe((response:any)=>{
      console.log(response);
    })
    this.onupdateAppointment=false;
  }


  onDeleteAppointment(appointId:any)
  {
    this.patientService.delAppointment(appointId).subscribe(
      (response:any)=>{
        console.log("appointment deleted succesfully",response)
      }
    )
  }


  isJoinVisible(start: string, expiresAt: number): boolean {
    const appointmentTime = new Date(start);
    const currentTime = new Date();
    return appointmentTime.getTime() <= currentTime.getTime() && currentTime.getTime() <= expiresAt;
  }
}

