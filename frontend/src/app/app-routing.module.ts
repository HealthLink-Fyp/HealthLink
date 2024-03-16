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
  {path:'pboard',component:patientDashBoard}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
