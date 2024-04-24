import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { BodychartComponent } from './bodychart.component';

const routes: Routes = [{ path: '', component: BodychartComponent }];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class BodychartRoutingModule { }
