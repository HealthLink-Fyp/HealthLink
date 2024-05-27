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
import { MaterialModule } from 'src/app/architecture/material/material/material.module';

import { BarchartComponent } from './barchart/barchart.component';
import { NgxEchartsModule } from 'ngx-echarts';
import { MstoreComponent } from './mstore/mstore.component';
import { LabtestsComponent } from './labtests/labtests.component';
import { SettingsComponent } from './settings/settings.component';
import { MedrecordComponent } from './medrecord/medrecord.component';
import { VideocallComponent } from './videocall/videocall.component';
import { ChatComponent } from './chat/chat.component';
import { DialogComponent } from './videocall/dialog/dialog.component';
import { PaymentComponent } from './payment/payment.component';
import { GooglePayButtonModule } from '@google-pay/button-angular';
import { LandingModule } from '../../topnav/landing.module';




@NgModule({
  declarations: [BarchartComponent,BodychartComponent,DocsearchComponent,PappointmentComponent,PformComponent,PsidenavComponent,PtabsComponent,PatComponent, MstoreComponent, LabtestsComponent,SettingsComponent, MedrecordComponent,VideocallComponent,ChatComponent,DialogComponent, PaymentComponent],
  imports: [
    CommonModule,
    PatRoutingModule,
    MaterialModule,
    LandingModule,
    GooglePayButtonModule,
   
    NgxEchartsModule.forRoot({
      /**
       * This will import all modules from echarts.
       * If you only need custom modules,
       * please refer to [Custom Build] section.
       */
      echarts: () => import('echarts') // or import('./path-to-my-custom-echarts')
    }),

  ]
})
export class PatModule { }
