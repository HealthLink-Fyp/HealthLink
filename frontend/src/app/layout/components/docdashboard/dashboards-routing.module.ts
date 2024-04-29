import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DashboardsComponent } from './dashboards.component';

import { PsidenavComponent } from '../patdashboard/pat/psidenav/psidenav.component';
import { BodychartComponent } from '../patdashboard/pat/bodychart/bodychart.component';
import { BarchartComponent } from '../charts/barchart/barchart.component';
import { DsidenavComponent } from './doc/dsidenav/dsidenav.component';
import { DformComponent } from './doc/dform/dform.component';
import { PappointmentComponent } from '../patdashboard/pat/pappointment/pappointment.component';

const routes: Routes = [
  { path: '', component: DashboardsComponent },
  {path:'dashboard',component:DsidenavComponent},
  {path:'',component:BodychartComponent},
  {path:'',component:BarchartComponent},
  {path:'form',component:DformComponent},
 
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class DashboardsRoutingModule { }
