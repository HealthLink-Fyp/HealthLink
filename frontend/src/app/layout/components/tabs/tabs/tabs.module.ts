import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { TabsRoutingModule } from './tabs-routing.module';
import { TabsComponent } from './tabs.component';
import { MaterialModule } from 'src/app/material/material/material.module';
import { SignInUpModule } from '../../sign-in-up/sign-in-up.module';




@NgModule({
  declarations: [
    TabsComponent
  ],
  imports: [
    CommonModule,
    TabsRoutingModule,
    MaterialModule,
    SignInUpModule
  ]
})
export class TabsModule { }
