import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { PsidenavComponent } from './psidenav/psidenav.component';
import { BodychartComponent } from './bodychart/bodychart.component';
import { PappointmentComponent } from './pappointment/pappointment.component';
import { PformComponent } from './pform/pform.component';
import { BarchartComponent } from './barchart/barchart.component';
import { DocsearchComponent } from './docsearch/docsearch.component';


const routes: Routes = [
  {path:'dashboard',component:PsidenavComponent},
  {path:'',component:BodychartComponent},
  {path:'',component:BarchartComponent},
  {path:'form',component:PformComponent},
  {path:'',component:DocsearchComponent},
  {path:'/appointment/booking',component:PappointmentComponent}
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class PatRoutingModule { }
