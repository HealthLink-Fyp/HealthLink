import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DashboardsComponent } from './dashboards.component';


import { DsidenavComponent } from './doc/dsidenav/dsidenav.component';
import { DformComponent } from './doc/dform/dform.component';
import { VideocallComponent } from './videocall/videocall.component';
import { DappointmentComponent } from './doc/dappointment/dappointment.component';
import { AboutComponent } from './doc/about/about.component';
import { ChatComponent } from './chat/chat.component';
import { TodoComponent } from './doc/todo/todo.component';
import { SettingsComponent } from './settings/settings.component';



const routes: Routes = [
  { path: '', component: DashboardsComponent },
  {path:'dashboard',component:DsidenavComponent},
  {path:'form',component:DformComponent},
  {path:'videoCall',component:VideocallComponent},
  {path:'videoCall/:patientId/:doctorId',component:VideocallComponent},
  {path:'appointments',component:DappointmentComponent},
  {path:'about/:doctorId',component:AboutComponent},
  {path:'chat',component:ChatComponent},
  {path:'todo',component:TodoComponent},
  {path:'settings',component:SettingsComponent}

 
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class DashboardsRoutingModule { }
