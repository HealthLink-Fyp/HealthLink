import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { FooterRoutingModule } from './footer-routing.module';
import { FooterComponent } from './footer.component';

import {MatIconModule} from '@angular/material/icon';

@NgModule({
  declarations: [
    FooterComponent
  ],
  imports: [
    CommonModule,
    FooterRoutingModule,
    MatIconModule
  ]
})
export class FooterModule { }
