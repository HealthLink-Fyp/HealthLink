import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { SignInUpComponent } from './sign-in-up.component';

const routes: Routes = [{ path: '', component: SignInUpComponent }];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class SignInUpRoutingModule { }
