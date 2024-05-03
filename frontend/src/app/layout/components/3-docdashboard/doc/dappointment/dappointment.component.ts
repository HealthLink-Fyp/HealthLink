import { Component } from '@angular/core';
import { DoctorService } from 'src/app/architecture/services/doctor/doctor.service';

@Component({
  selector: 'app-dappointment',
  templateUrl: './dappointment.component.html',
  styleUrls: ['./dappointment.component.css']
})
export class DappointmentComponent {




  bookedAppointments:any[] = []; 

  constructor(private doctorService:DoctorService){}
  
  ngOnInit(): void {
 
   
  }
  

  onbookedAppointments() {
    this.doctorService.getbookedAppointments().subscribe(
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

  isJoinVisible(start: string, expiresAt: number): boolean {
    const appointmentTime = new Date(start);
    const currentTime = new Date();
    return appointmentTime.getTime() <= currentTime.getTime() && currentTime.getTime() <= expiresAt;
  }

  
  onDeleteAppointment(appointId:any)
  {
    this.doctorService.delAppointment(appointId).subscribe(
      (response:any)=>{
        console.log("appointment deleted succesfully",response)
      }
    )
  }
}
