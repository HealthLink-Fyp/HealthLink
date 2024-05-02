import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DashboardsComponent } from './dashboards.component';


import { DsidenavComponent } from './doc/dsidenav/dsidenav.component';
import { DformComponent } from './doc/dform/dform.component';
import { VideocallComponent } from './videocall/videocall.component';
import { DappointmentComponent } from './doc/dappointment/dappointment.component';


const routes: Routes = [
  { path: '', component: DashboardsComponent },
  {path:'dashboard',component:DsidenavComponent},
  {path:'form',component:DformComponent},
  {path:'videoCall',component:VideocallComponent},
  {path:'videoCall/:patientId/:doctorId',component:VideocallComponent},
  {path:'appointments',component:DappointmentComponent},
 
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class DashboardsRoutingModule { }
