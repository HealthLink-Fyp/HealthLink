import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { PatRoutingModule } from './pat-routing.module';
import { BodychartComponent } from './bodychart/bodychart.component';
import { PappointmentComponent } from './pappointment/pappointment.component';
import { PformComponent } from './pform/pform.component';
import { PsidenavComponent } from './psidenav/psidenav.component';
import { PtabsComponent } from './ptabs/ptabs.component';
import { PatComponent } from './pat.component';
import { DocsearchComponent } from './docsearch/docsearch.component';
import { MaterialModule } from 'src/app/material/material/material.module';
import { SharechartModule } from '../../charts/barchart/sharechart/sharechart.module';
import { BarchartComponent } from '../../charts/barchart/barchart.component';


@NgModule({
  declarations: [BodychartComponent,DocsearchComponent,PappointmentComponent,PformComponent,PsidenavComponent,PtabsComponent,PatComponent],
  imports: [
    CommonModule,
    PatRoutingModule,
    MaterialModule,
    SharechartModule,
    BarchartComponent
  ]
})
export class PatModule { }
