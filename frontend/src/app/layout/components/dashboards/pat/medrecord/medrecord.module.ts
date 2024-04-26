import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { MedrecordRoutingModule } from './medrecord-routing.module';
import { MedrecordComponent } from './medrecord.component';


@NgModule({
  declarations: [
    MedrecordComponent
  ],
  imports: [
    CommonModule,
    MedrecordRoutingModule
  ]
})
export class MedrecordModule { }
