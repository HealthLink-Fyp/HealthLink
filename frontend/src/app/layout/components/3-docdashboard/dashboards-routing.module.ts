import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DashboardsComponent } from './dashboards.component';


import { DsidenavComponent } from './doc/dsidenav/dsidenav.component';
import { DformComponent } from './doc/dform/dform.component';


const routes: Routes = [
  { path: '', component: DashboardsComponent },
  {path:'dashboard',component:DsidenavComponent},
  {path:'form',component:DformComponent},
 
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class DashboardsRoutingModule { }
