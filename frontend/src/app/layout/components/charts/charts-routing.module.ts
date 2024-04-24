import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ChartsComponent } from './charts.component';
import { BarchartComponent } from './barchart/barchart.component';

const routes: Routes = [
  { path: '', component: ChartsComponent },
  {path:'bar',component:BarchartComponent}
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class ChartsRoutingModule { }
