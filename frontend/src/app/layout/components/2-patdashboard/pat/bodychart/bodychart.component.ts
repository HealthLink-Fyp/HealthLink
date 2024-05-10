import { Component, OnInit } from '@angular/core';
import { PatientService } from 'src/app/architecture/services/patient/patient.service';

@Component({
  selector: 'app-bodychart',
  templateUrl: './bodychart.component.html',
  styleUrls: ['./bodychart.component.css']
})
export class BodychartComponent implements OnInit {
  showInfoPanel: boolean = false;
  infoText: string = '';
  responseData:any=''

  constructor(private vMetrices:PatientService){}

  ngOnInit(): void {
    this.vMetrices.getMetrices().subscribe((res:any)=>{
      console.log("hi iam visuals",res);
      this.responseData = res; // store the response data in a component property
    })
  }

  showInfo(bodyPart: string) {
    this.showInfoPanel = true;
    // Example information for body parts
    switch (bodyPart) {
      case 'Chest':
        this.infoText = this.responseData.symptoms.find((symptom:any) => symptom.body_part === 'Chest').symptoms.map((symptom:any) => symptom.symptom).join(', ');
        break;
      case 'Arms, Jaw, Back':
        this.infoText = this.responseData.symptoms.find((symptom:any) => symptom.body_part === 'Arms, Jaw, Back').symptoms.map((symptom :any)=> symptom.symptom).join(', ');
        break;
      // Add more cases for other body parts
    }
  }

  hideInfo() {
    this.showInfoPanel = false;
  }
}
