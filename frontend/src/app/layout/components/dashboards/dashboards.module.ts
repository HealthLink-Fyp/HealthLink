import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { DashboardsRoutingModule } from './dashboards-routing.module';
import { DashboardsComponent } from './dashboards.component';
import { DocComponent } from './doc/doc.component';
import { PatComponent } from './pat/pat.component';
import { PsidenavComponent } from './pat/psidenav/psidenav.component';
import { PtabsComponent } from './pat/ptabs/ptabs.component';
import { DsidenavComponent } from './doc/dsidenav/dsidenav.component';
import { BarchartComponent } from '../charts/barchart/barchart.component';
import { ChartsModule } from '../charts/charts.module';
import { BodychartComponent } from '../bodychart/bodychart.component';
import { BodychartModule } from '../bodychart/bodychart.module';
import { MaterialModule } from 'src/app/material/material/material.module';
import { CardsModule } from '../cards/cards.module';


@NgModule({
  declarations: [
    DashboardsComponent,
    DocComponent,
    PatComponent,
    PsidenavComponent,
    PtabsComponent,
    DsidenavComponent
  ],
  imports: [
    CommonModule,
    DashboardsRoutingModule,
    BodychartModule,
    MaterialModule,
    ChartsModule,
    
  ]
})
export class DashboardsModule { }
