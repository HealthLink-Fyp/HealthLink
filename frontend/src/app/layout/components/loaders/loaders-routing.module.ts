import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoadersComponent } from './loaders.component';

const routes: Routes = [{ path: '', component: LoadersComponent }];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class LoadersRoutingModule { }
