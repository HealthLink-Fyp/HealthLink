import { HttpClient } from '@angular/common/http';
import { Component } from '@angular/core';
import { PatientService } from 'src/app/architecture/services/patient/patient.service';

@Component({
  selector: 'app-medrecord',
  templateUrl: './medrecord.component.html',
  styleUrls: ['./medrecord.component.css']
})
export class MedrecordComponent {
  doctorNotes:any='';
  pastRecords:any='' ;
  viewRecords:boolean=false;

  constructor(private recordsService: PatientService) { }

  ngOnInit(): void {
    this.recordsService.getRecords().subscribe((res:any)=>{
      this.doctorNotes = res.results[3].doctor_notes;
      this.pastRecords = res.results[3].past_records;
    })
  }

}
