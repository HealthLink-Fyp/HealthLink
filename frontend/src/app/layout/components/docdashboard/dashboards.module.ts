import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { DashboardsRoutingModule } from './dashboards-routing.module';
import { DashboardsComponent } from './dashboards.component';
import { DocComponent } from './doc/doc.component';


import { DsidenavComponent } from './doc/dsidenav/dsidenav.component';
import { BarchartComponent } from '../charts/barchart/barchart.component';


import { MaterialModule } from 'src/app/architecture/material/material/material.module';





import { DformComponent } from './doc/dform/dform.component';

import { SharechartModule } from '../charts/barchart/sharechart/sharechart.module';
import { DtabsComponent } from './doc/dtabs/dtabs.component';



@NgModule({
  declarations: [
    DashboardsComponent,
    DocComponent,
    DsidenavComponent,
    BarchartComponent,
    DformComponent,
    DtabsComponent,


    
  ],
  imports: [
    CommonModule,
    DashboardsRoutingModule,
    MaterialModule,
    SharechartModule,
  
    
   
  ],
 
})
export class DashboardsModule { }
