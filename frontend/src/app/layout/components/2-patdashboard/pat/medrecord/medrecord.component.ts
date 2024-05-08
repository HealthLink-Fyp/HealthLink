import { HttpClient } from '@angular/common/http';
import { Component } from '@angular/core';
import { MatTableDataSource } from '@angular/material/table';
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

  results = [];
  dataSource = new MatTableDataSource(this.results);

  constructor(private recordsService: PatientService) { }

  ngOnInit(): void {
    this.recordsService.getRecords().subscribe((res:any)=>{
      this.results = res.results;
      this.dataSource.data = this.results;
    })
  }

  onPageChange(event: any) {
    const startIndex = event.pageIndex * event.pageSize;
    let endIndex = startIndex + event.pageSize;
    if (endIndex > this.results.length) {
      endIndex = this.results.length;
    }
    this.dataSource.data = this.results.slice(startIndex, endIndex);
  }

}
