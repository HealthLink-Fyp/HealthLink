import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { PsidenavComponent } from './psidenav/psidenav.component';
import { BodychartComponent } from './bodychart/bodychart.component';
import { PappointmentComponent } from './pappointment/pappointment.component';
import { PformComponent } from './pform/pform.component';
import { BarchartComponent } from './barchart/barchart.component';
import { DocsearchComponent } from './docsearch/docsearch.component';
import { MstoreComponent } from './mstore/mstore.component';
import { LabtestsComponent } from './labtests/labtests.component';
import { SettingsComponent } from './settings/settings.component';
import { MedrecordComponent } from './medrecord/medrecord.component';
import { VideocallComponent } from './videocall/videocall.component';
import { PaymentComponent } from './payment/payment.component';
import { ChatComponent } from './chat/chat.component';



const routes: Routes = [
  {path:'dashboard',component:PsidenavComponent},
  {path:'',component:BodychartComponent},
  {path:'',component:BarchartComponent},
  {path:'form',component:PformComponent},
  {path:'docsearch',component:DocsearchComponent},
  {path:'appointments',component:PappointmentComponent},
  {path:'appointments/:doctorId',component:PappointmentComponent},
  {path:'medicalStore',component:MstoreComponent},
  {path:'labTests',component:LabtestsComponent},
  {path:'settings',component:SettingsComponent},
  {path:'medRecords',component:MedrecordComponent},
  {path:'videoCall',component:VideocallComponent},
  {path:'chat',component:ChatComponent},
  {path:'payment',component:PaymentComponent},
  {path:'payment/:doctorId',component:PaymentComponent}
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class PatRoutingModule { }
