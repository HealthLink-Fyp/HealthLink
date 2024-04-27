import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LoginComponent } from './auth/login/login.component';
import { RegisterComponent } from './auth/register/register.component';
import { NavComponent } from './auth/nav/nav.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { RouterOutlet } from '@angular/router';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HTTP_INTERCEPTORS, HttpClientModule, provideHttpClient, withInterceptors } from '@angular/common/http';
import { AuthInterceptor } from './interceptors/auth.interceptor';
import { AuthComponent } from './auth/auth/auth.component';
import { ResetComponent } from './auth/auth/reset/reset.component';
import { ForgotComponent } from './auth/auth/forgot/forgot.component';
import { DoctorComponent } from './doctor/doctor.component';
import { PatientComponent } from './patient/patient.component';
import { DashboardComponent as patientDashboard } from './patient/dashboard/dashboard/dashboard.component';
import { DashboardComponent as doctorDashboard } from './doctor/dashboard/dashboard/dashboard.component';
import { CommonModule } from '@angular/common';
import { STEPPER_GLOBAL_OPTIONS } from '@angular/cdk/stepper';
import { FlexLayoutModule } from '@angular/flex-layout';
import { ChatComponent } from './chat/chat.component';
import { VideocallComponent } from './videocall/videocall.component';
import { TranscriptionComponent } from './videocall/transcription/transcription.component';
import { MaterialModule } from './material/material/material.module';
import { DialogComponent } from './videocall/dialog/dialog.component';
import { PformComponent } from './layout/components/dashboards/pat/pform/pform.component';

import { provideHttpCache, withHttpCacheInterceptor } from '@ngneat/cashew';
import { DocsearchComponent } from './layout/components/dashboards/pat/docsearch/docsearch.component';
import { DformComponent } from './layout/components/dashboards/doc/dform/dform.component';



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
    VideocallComponent,
    TranscriptionComponent,
    DialogComponent,
    PformComponent,
    DocsearchComponent,
    DformComponent

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
