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

  constructor(private vMetrices:PatientService){}

  ngOnInit(): void {
    this.vMetrices.getMetrices().subscribe((res:any)=>{
      console.log("hi iam visuals",res);
    })
  }

  showInfo(bodyPart: string) {
    this.showInfoPanel = true;
    // Example information for body parts
    switch (bodyPart) {
      case 'Head':
        this.infoText = 'This is the head.';
        break;
      case 'Stomach':
        this.infoText = 'This is the Stomach.';
        break;
      // Add more cases for other body parts
    }
  }

  hideInfo() {
    this.showInfoPanel = false;
  }
}
