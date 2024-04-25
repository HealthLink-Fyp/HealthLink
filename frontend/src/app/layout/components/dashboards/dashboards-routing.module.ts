import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DashboardsComponent } from './dashboards.component';
import { PatComponent } from './pat/pat.component';
import { PsidenavComponent } from './pat/psidenav/psidenav.component';

const routes: Routes = [
  { path: '', component: DashboardsComponent },
  {path:'pat',component:PsidenavComponent}
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class DashboardsRoutingModule { }
