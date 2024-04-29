import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { DashboardsRoutingModule } from './dashboards-routing.module';
import { DashboardsComponent } from './dashboards.component';
import { DocComponent } from './doc/doc.component';
import { PatComponent } from '../patdashboard/pat/pat.component';
import { PsidenavComponent } from '../patdashboard/pat/psidenav/psidenav.component';
import { PtabsComponent } from '../patdashboard/pat/ptabs/ptabs.component';
import { DsidenavComponent } from './doc/dsidenav/dsidenav.component';
import { BarchartComponent } from '../charts/barchart/barchart.component';

import { BodychartComponent } from '../patdashboard/pat/bodychart/bodychart.component';

import { MaterialModule } from 'src/app/material/material/material.module';

import { NgxEchartsModule } from 'ngx-echarts';


import { PformComponent} from '../patdashboard/pat/pform/pform.component';
import { DocsearchComponent } from '../patdashboard/pat/docsearch/docsearch.component';
import { DformComponent } from './doc/dform/dform.component';
import { AboutComponent } from './doc/about/about.component';
import { PappointmentComponent } from '../patdashboard/pat/pappointment/pappointment.component';
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
  exports:[PsidenavComponent]
})
export class DashboardsModule { }
