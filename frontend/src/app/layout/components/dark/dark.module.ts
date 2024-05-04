import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { DarkRoutingModule } from './dark-routing.module';
import { DarkComponent } from './dark.component';

import {MatSlideToggleModule} from '@angular/material/slide-toggle';


@NgModule({
  declarations: [
    DarkComponent
  ],
  imports: [
    CommonModule,
    DarkRoutingModule,
    MatSlideToggleModule
  ]
})
export class DarkModule { }
