import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LoginComponent } from './architecture/auth/login/login.component';
import { RegisterComponent } from './architecture/auth/register/register.component';
import { NavComponent } from './architecture/auth/nav/nav.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { RouterOutlet } from '@angular/router';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HTTP_INTERCEPTORS, HttpClientModule, provideHttpClient, withInterceptors } from '@angular/common/http';
import { AuthInterceptor } from './architecture/interceptors/auth.interceptor';
import { AuthComponent } from './architecture/auth/auth/auth.component';
import { ResetComponent } from './architecture/auth/auth/reset/reset.component';
import { ForgotComponent } from './architecture/auth/auth/forgot/forgot.component';
import { DoctorComponent } from './architecture/doctor/doctor.component';
import { PatientComponent } from './architecture/patient/patient.component';
import { DashboardComponent as patientDashboard } from './architecture/patient/dashboard/dashboard/dashboard.component';
import { DashboardComponent as doctorDashboard } from './architecture/doctor/dashboard/dashboard/dashboard.component';
import { CommonModule } from '@angular/common';
import { STEPPER_GLOBAL_OPTIONS } from '@angular/cdk/stepper';
import { FlexLayoutModule } from '@angular/flex-layout';
import { ChatComponent } from './architecture/chat/chat.component';

import { provideHttpCache, withHttpCacheInterceptor } from '@ngneat/cashew';

import { AboutComponent } from './layout/components/3-docdashboard/doc/about/about.component';
import { MaterialModule } from './architecture/material/material/material.module';




@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    RegisterComponent,
    NavComponent,
    AuthComponent,
    ResetComponent,
    ForgotComponent,
    DoctorComponent,
    PatientComponent,
    patientDashboard,
    doctorDashboard,
    ChatComponent,
    

  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    RouterOutlet,
    ReactiveFormsModule,
    HttpClientModule,
    FormsModule,
    CommonModule,
    FlexLayoutModule,
    AppRoutingModule,
    MaterialModule,
  

   
  ],

  
  providers: [
    {
      provide: STEPPER_GLOBAL_OPTIONS,
      useValue: {displayDefaultIndicatorType: false},
    },
    {
      provide: HTTP_INTERCEPTORS,
      useClass: AuthInterceptor,
      multi: true,
    },
    provideHttpClient(withInterceptors([withHttpCacheInterceptor()])),
    provideHttpCache(),
 
  ],
  bootstrap: [AppComponent],
})
export class AppModule {}
