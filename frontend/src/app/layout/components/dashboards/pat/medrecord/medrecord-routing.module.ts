import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { MedrecordComponent } from './medrecord.component';

const routes: Routes = [{ path: '', component: MedrecordComponent }];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class MedrecordRoutingModule { }
