import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DashboardsComponent } from './dashboards.component';

import { PsidenavComponent } from './pat/psidenav/psidenav.component';
import { BodychartComponent } from './charts/bodychart/bodychart.component';
import { BarchartComponent } from './charts/barchart/barchart.component';
import { DsidenavComponent } from './doc/dsidenav/dsidenav.component';
import { DformComponent } from './doc/dform/dform.component';
import { PappointmentComponent } from './pat/pappointment/pappointment.component';

const routes: Routes = [
  { path: '', component: DashboardsComponent },
  {path:'patient',component:PsidenavComponent},
  {path:'doctor',component:DsidenavComponent},
  {path:'',component:BodychartComponent},
  {path:'',component:BarchartComponent},
  {path:'dform',component:DformComponent},
  {path:'patient/appointment/booking',component:PappointmentComponent}
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class DashboardsRoutingModule { }
