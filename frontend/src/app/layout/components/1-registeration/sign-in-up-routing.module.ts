import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { SignInUpComponent } from './sign-in-up.component';
import { LoginComponent } from './login/login.component';

const routes: Routes = [
  { path: 'Sign-up', component: SignInUpComponent },
  { path: 'login', component:LoginComponent },
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class SignInUpRoutingModule { }
