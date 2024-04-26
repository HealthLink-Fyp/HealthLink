import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AuthComponent } from './auth/auth/auth.component';
import { LoginComponent } from './auth/login/login.component';
import { RegisterComponent } from './auth/register/register.component';
import { ForgotComponent } from './auth/auth/forgot/forgot.component';
import { ResetComponent } from './auth/auth/reset/reset.component';
import { DoctorComponent } from './doctor/doctor.component';
import { PatientComponent } from './patient/patient.component';
import { DashboardComponent as doctorDashBoard } from './doctor/dashboard/dashboard/dashboard.component';
import { DashboardComponent as patientDashBoard } from './patient/dashboard/dashboard/dashboard.component';


const routes: Routes = [
  { path: '', component: AuthComponent },
  { path: 'login', component: LoginComponent },
  { path: 'register', component: RegisterComponent },
  { path: 'forgot', component: ForgotComponent },
  { path: 'reset/:token', component: ResetComponent },

  { path: 'doctor', component: DoctorComponent },
  { path: 'patient', component: PatientComponent },
  {path:'dboard',component:doctorDashBoard},
  {path:'pboard',component:patientDashBoard},

  {path:'dboard/:userId',component:doctorDashBoard},





  //materialui

  
  // { path: 'bodychart', loadChildren: () => import('./layout/components/dashboards/bodychart/bodychart.module').then(m => m.BodychartModule) },
  // { path: 'cards', loadChildren: () => import('./layout/components/layout/cards/cards.module').then(m => m.CardsModule) },
  // { path: 'charts', loadChildren: () => import('./layout/components/charts/charts.module').then(m => m.ChartsModule) },
  { path: 'dark', loadChildren: () => import('./layout/components/dark/dark.module').then(m => m.DarkModule) },
  // { path: 'footer', loadChildren: () => import('./layout/components/layout/footer/footer.module').then(m => m.FooterModule) },
  { path: 'topnav', loadChildren: () => import('./layout/components/topnav/landing.module').then(m => m.LandingModule) },
  { path: 'lay', loadChildren: () => import('./layout/components/layout/layout.module').then(m => m.LayoutModule) },
  { path: 'list', loadChildren: () => import('./layout/components/list/list.module').then(m => m.ListModule) },
  { path: 'loaders', loadChildren: () => import('./layout/components/loaders/loaders.module').then(m => m.LoadersModule) },
  { path: 'notification', loadChildren: () => import('./layout/components/notification/notification.module').then(m => m.NotificationModule) },
  { path: 'search-suggest', loadChildren: () => import('./layout/components/search-suggest/search-suggest.module').then(m => m.SearchSuggestModule) },
  { path: 'searchbar', loadChildren: () => import('./layout/components/searchbar/searchbar.module').then(m => m.SearchbarModule) },
  { path: 'sidenav', loadChildren: () => import('./layout/components/sidenav/sidenav.module').then(m => m.SidenavModule) },
  // { path: 'sign-in-up', loadChildren: () => import('./layout/components/sign-in-up/sign-in-up.module').then(m => m.SignInUpModule) },
  { path: 'stepper', loadChildren: () => import('./layout/components/stepper/stepper.module').then(m => m.StepperModule) },
  // { path: 'swipe', loadChildren: () => import('./layout/components/layout/swipe/swipe.module').then(m => m.SwipeModule) },
  { path: 'dashboard', loadChildren: () => import('./layout/components/dashboards/dashboards.module').then(m => m.DashboardsModule) },
  { path: 'account', loadChildren: () => import('./layout/components/tabs/tabs/tabs.module').then(m => m.TabsModule) },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
