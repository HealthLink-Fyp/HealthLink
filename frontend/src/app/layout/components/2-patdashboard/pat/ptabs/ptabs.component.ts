import { Component, OnInit } from '@angular/core';
import { MatSort, Sort } from '@angular/material/sort';
import { PatientService } from 'src/app/architecture/services/patient/patient.service';

@Component({
  selector: 'app-ptabs',
  templateUrl: './ptabs.component.html',
  styleUrls: ['./ptabs.component.css']
})
export class PtabsComponent implements OnInit {
  bookedAppointments:any[] = []; 
  sortedData:any[]=[];

  ngOnInit(): void
  {
   this.onbookedAppointments();
  }

  constructor(private patientService:PatientService){}

  onbookedAppointments() {
    this.patientService.getbookedAppointments().subscribe(
      (response: any) => {
        this.bookedAppointments = response;
        this.sortedData = this.bookedAppointments.slice();
      
      }
    );
  }

  sortData(event: Sort) {
    const sort = event.direction;
    const data = this.bookedAppointments.slice();
    if (sort === 'asc') {
      data.sort((a, b) => a.doctor - b.doctor);
    } else if (sort === 'desc') {
      data.sort((a, b) => b.doctor - a.doctor);
    }
    this.sortedData = data;
  }
}
