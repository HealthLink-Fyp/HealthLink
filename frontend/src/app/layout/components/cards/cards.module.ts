import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { CardsRoutingModule } from './cards-routing.module';
import { CardsComponent } from './cards.component';
import { MatCardModule } from '@angular/material/card';
import { MaterialModule } from 'src/app/material/material/material.module';
import { Card1Component } from './card1/card1.component';

@NgModule({
  declarations: [
    CardsComponent,
    Card1Component
  ],
  imports: [
    CommonModule,
    CardsRoutingModule,
    MaterialModule
  ],
  exports:[Card1Component]
})
export class CardsModule { }
