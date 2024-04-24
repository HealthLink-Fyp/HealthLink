import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { BodychartRoutingModule } from './bodychart-routing.module';
import { BodychartComponent } from './bodychart.component';


@NgModule({
  declarations: [
    BodychartComponent
  ],
  imports: [
    CommonModule,
    BodychartRoutingModule
  ]
})
export class BodychartModule { }
