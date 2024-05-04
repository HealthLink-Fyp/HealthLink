import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DarkComponent } from './dark.component';

const routes: Routes = [{ path: '', component: DarkComponent }];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class DarkRoutingModule { }
