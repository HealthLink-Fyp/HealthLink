import { Component } from '@angular/core';
import { DoctorService } from 'src/app/architecture/services/doctor/doctor.service';
import { Location } from '@angular/common';

@Component({
  selector: 'app-dappointment',
  templateUrl: './dappointment.component.html',
  styleUrls: ['./dappointment.component.css']
})
export class DappointmentComponent {


  displayedColumns: string[] = ['scheduledTime', 'endingTime', 'status', 'actions'];

  bookedAppointments:any[] = []; 

  constructor(private doctorService:DoctorService, private location: Location){}
  
  ngOnInit(): void {
    this.onbookedAppointments();
   
  }

  goBack(): void {
    this.location.back();
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

        // Sort the appointments by the latest scheduled time
        this.bookedAppointments.sort((a, b) => {
          return new Date(b.start).getTime() - new Date(a.start).getTime();
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
