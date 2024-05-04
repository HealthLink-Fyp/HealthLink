import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { SignInUpRoutingModule } from './sign-in-up-routing.module';
import { SignInUpComponent } from './sign-in-up.component';

import { MaterialModule } from 'src/app/architecture/material/material/material.module';
import { LoginComponent } from './login/login.component';
import { ReactiveFormsModule } from '@angular/forms';
import { NotificationModule } from '../notification/notification.module';


@NgModule({
  declarations: [
    SignInUpComponent,
    LoginComponent
  ],
  imports: [
    CommonModule,
    SignInUpRoutingModule,
    MaterialModule,
    ReactiveFormsModule,
    NotificationModule

  ],
  exports:[SignInUpComponent,LoginComponent]
})

export class SignInUpModule { }
