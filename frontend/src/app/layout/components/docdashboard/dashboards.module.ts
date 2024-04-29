import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { DashboardsRoutingModule } from './dashboards-routing.module';
import { DashboardsComponent } from './dashboards.component';
import { DocComponent } from './doc/doc.component';

import { PsidenavComponent } from '../patdashboard/pat/psidenav/psidenav.component';

import { DsidenavComponent } from './doc/dsidenav/dsidenav.component';
import { BarchartComponent } from '../charts/barchart/barchart.component';

import { BodychartComponent } from '../patdashboard/pat/bodychart/bodychart.component';

import { MaterialModule } from 'src/app/architecture/material/material/material.module';





import { DformComponent } from './doc/dform/dform.component';

import { SharechartModule } from '../charts/barchart/sharechart/sharechart.module';



@NgModule({
  declarations: [
    DashboardsComponent,
    DocComponent,
    DsidenavComponent,
    BodychartComponent,
    BarchartComponent,
    DformComponent,


    
  ],
  imports: [
    CommonModule,
    DashboardsRoutingModule,
    MaterialModule,
    SharechartModule,
    BarchartComponent
    
   
  ],
 
})
export class DashboardsModule { }
