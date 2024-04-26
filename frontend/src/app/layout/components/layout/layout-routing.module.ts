import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LayoutComponent } from './layout.component';
import { Lay1Component } from './landing/lay1.component';
import { CardsComponent } from './cards/cards.component';
import { Card1Component } from './cards/card1/card1.component';
import { FooterComponent } from './footer/footer.component';
import { SwipeComponent } from './swipe/swipe.component';

const routes: Routes = [
  { path: '', component: LayoutComponent },
  {path:'landingPage',component:Lay1Component},
  {path:'',component:CardsComponent},
  {path:'',component:Card1Component},
  {path:'',component:FooterComponent},
  {path:'',component:SwipeComponent}
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class LayoutRoutingModule { }
