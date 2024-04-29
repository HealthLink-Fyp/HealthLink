import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { AuthRoutingModule } from './auth-routing.module';
import { AuthComponent } from './auth.component';
import { ForgotComponent } from './forgot/forgot.component';
import { ResetComponent } from './reset/reset.component';

@NgModule({
  declarations: [AuthComponent, ForgotComponent, ResetComponent],
  imports: [CommonModule, AuthRoutingModule],
})
export class AuthModule {}
