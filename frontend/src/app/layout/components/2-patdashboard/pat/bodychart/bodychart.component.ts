import { Component } from '@angular/core';

@Component({
  selector: 'app-bodychart',
  templateUrl: './bodychart.component.html',
  styleUrls: ['./bodychart.component.css']
})
export class BodychartComponent {
  showInfoPanel: boolean = false;
  infoText: string = '';

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
