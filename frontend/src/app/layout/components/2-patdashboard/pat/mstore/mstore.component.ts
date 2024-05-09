import { Component, OnInit } from '@angular/core';
import { PatientService } from 'src/app/architecture/services/patient/patient.service';

@Component({
  selector: 'app-mstore',
  templateUrl: './mstore.component.html',
  styleUrls: ['./mstore.component.css']
})
export class MstoreComponent implements OnInit {

  medicines:any = [];
  totalResults = 0;

  constructor(private medicineService:PatientService){}

  ngOnInit(): void {
       this.getMedicines(0);
    
  }

  getMedicines(offset: number) {
    this.medicineService.getMedicines(10, offset).subscribe((response: any) => {
      this.medicines = response.results;
      this.totalResults = response.count;
    });
  }

  onPageChange(event: any) {
    this.getMedicines(event.pageIndex * event.pageSize);
  }

 

 


}
