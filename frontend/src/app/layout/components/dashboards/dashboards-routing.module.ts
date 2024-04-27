import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DashboardsComponent } from './dashboards.component';

import { PsidenavComponent } from './pat/psidenav/psidenav.component';
import { BodychartComponent } from './charts/bodychart/bodychart.component';
import { BarchartComponent } from './charts/barchart/barchart.component';

const routes: Routes = [
  { path: '', component: DashboardsComponent },
  {path:'patient',component:PsidenavComponent},
  {path:'',component:BodychartComponent},
  {path:'',component:BarchartComponent}
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class DashboardsRoutingModule { }
