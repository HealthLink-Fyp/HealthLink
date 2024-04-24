import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { SignInUpRoutingModule } from './sign-in-up-routing.module';
import { SignInUpComponent } from './sign-in-up.component';

import { MatRadioModule } from '@angular/material/radio';
import {MatSelectModule} from '@angular/material/select';
import { MatCardModule } from '@angular/material/card';

@NgModule({
  declarations: [
    SignInUpComponent
  ],
  imports: [
    CommonModule,
    SignInUpRoutingModule,
    MatRadioModule,
    MatSelectModule,
    MatCardModule
  ]
})
export class SignInUpModule { }
