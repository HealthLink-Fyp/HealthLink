import { Component } from '@angular/core';
import { DoctorService } from 'src/app/architecture/services/doctor/doctor.service';

@Component({
  selector: 'app-dappointment',
  templateUrl: './dappointment.component.html',
  styleUrls: ['./dappointment.component.css']
})
export class DappointmentComponent {


  doctorKey:any='';

  constructor(private doctorService:DoctorService){}
  
  ngOnInit(): void {
    this.doctorService.getDoctor().subscribe((res: any) => {
      this.doctorKey = res.user;
      console.log("coming from appointment doctor", this.doctorKey);
      console.log("the doctor id captured in appointment is : ", this.doctorKey);
    });
   
  }
  
}
