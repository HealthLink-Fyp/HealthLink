import { Component, OnInit } from '@angular/core';
import { PatientService } from 'src/app/services/patient/patient.service';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {

  patientData: any = {};


ngOnInit(): void {
  this.patientService.getPatient().subscribe((res:any)=>{
    this.patientData=res;
    console.log("coming from dashboard",this.patientData);
  }
    
  )
}

  constructor(private patientService:PatientService){}

  searchQuery:string='';
  searchResults:any[]=[];

  searchDoctors()
  {
    this.patientService.searchDoctors(this.searchQuery).subscribe(
      (response:any)=>{
          this.searchResults=response.results
      }
    )
    }

    

}
