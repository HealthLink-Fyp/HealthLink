import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CardsComponent } from './cards.component';
import { Card1Component } from './card1/card1.component';

const routes: Routes = [
  { path: '', component: CardsComponent },
  {path:'card1',component:Card1Component}
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class CardsRoutingModule { }
