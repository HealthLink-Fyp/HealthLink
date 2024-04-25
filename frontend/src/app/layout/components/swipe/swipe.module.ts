import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { SwipeRoutingModule } from './swipe-routing.module';
import { SwipeComponent } from './swipe.component';
import { MaterialModule } from 'src/app/material/material/material.module';


@NgModule({
  declarations: [
    SwipeComponent
  ],
  imports: [
    CommonModule,
    SwipeRoutingModule,
  ],
  exports:[SwipeComponent]
})
export class SwipeModule { }
