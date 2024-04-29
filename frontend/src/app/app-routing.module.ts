import { Component, NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AuthComponent } from './architecture/auth/auth/auth.component';
import { LoginComponent } from './architecture/auth/login/login.component';
import { RegisterComponent } from './architecture/auth/register/register.component';
import { ForgotComponent } from './architecture/auth/auth/forgot/forgot.component';
import { ResetComponent } from './architecture/auth/auth/reset/reset.component';
import { DoctorComponent } from './architecture/doctor/doctor.component';
import { PatientComponent } from './architecture/patient/patient.component';
import { DashboardComponent as doctorDashBoard } from './architecture/doctor/dashboard/dashboard/dashboard.component';
import { DashboardComponent as patientDashBoard } from './architecture/patient/dashboard/dashboard/dashboard.component';
import { ChatComponent } from './architecture/chat/chat.component';
import { VideocallComponent } from './architecture/videocall/videocall.component';
import { TranscriptionComponent } from './architecture/videocall/transcription/transcription.component';
import { AboutComponent } from './layout/components/docdashboard/doc/about/about.component';



const routes: Routes = [
  { path: 'auth', component: AuthComponent },
  { path: 'login', component: LoginComponent },
  { path: 'register', component: RegisterComponent },
  { path: 'forgot', component: ForgotComponent },
  { path: 'reset/:token', component: ResetComponent },

  { path: 'doctor', component: DoctorComponent },
  { path: 'patient', component: PatientComponent },
  {path:'dboard',component:doctorDashBoard},
  {path:'pboard',component:patientDashBoard},

  {path:'dboard/:userId',component:doctorDashBoard},

  {path:'chat',component:ChatComponent},

  {path:'call',component:VideocallComponent},


    {path:'dashboard/doctor/about/:userId',component:AboutComponent},

    {path:'voice',component:TranscriptionComponent},

  //materialui

  
  
  { path: 'dark', loadChildren: () => import('./layout/components/dark/dark.module').then(m => m.DarkModule) },
 
  { path: 'topnav', loadChildren: () => import('./layout/components/topnav/landing.module').then(m => m.LandingModule) },
  { path: '', loadChildren: () => import('./layout/components/layout/layout.module').then(m => m.LayoutModule) },
  { path: 'list', loadChildren: () => import('./layout/components/list/list.module').then(m => m.ListModule) },
  { path: 'loaders', loadChildren: () => import('./layout/components/loaders/loaders.module').then(m => m.LoadersModule) },
  { path: 'notification', loadChildren: () => import('./layout/components/notification/notification.module').then(m => m.NotificationModule) },
  { path: 'search-suggest', loadChildren: () => import('./layout/components/search-suggest/search-suggest.module').then(m => m.SearchSuggestModule) },
  { path: 'searchbar', loadChildren: () => import('./layout/components/searchbar/searchbar.module').then(m => m.SearchbarModule) },
  { path: 'sidenav', loadChildren: () => import('./layout/components/sidenav/sidenav.module').then(m => m.SidenavModule) },
  
  { path: 'stepper', loadChildren: () => import('./layout/components/stepper/stepper.module').then(m => m.StepperModule) },
 
  { path: 'doctor', loadChildren: () => import('./layout/components/docdashboard/dashboards.module').then(m => m.DashboardsModule) },
  { path: 'patient', loadChildren: () => import('./layout/components/patdashboard/pat/pat.module').then(m => m.PatModule) },
  { path: 'account', loadChildren: () => import('./layout/components/tabs/tabs/tabs.module').then(m => m.TabsModule) },
 
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
