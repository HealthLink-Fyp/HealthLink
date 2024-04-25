import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LayoutComponent } from './layout.component';
import { Lay1Component } from './lay1/lay1.component';

const routes: Routes = [
  { path: '', component: LayoutComponent },
  {path:'lay1',component:Lay1Component}
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class LayoutRoutingModule { }
