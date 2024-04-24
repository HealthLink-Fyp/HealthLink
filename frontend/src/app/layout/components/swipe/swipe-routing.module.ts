import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { SwipeComponent } from './swipe.component';

const routes: Routes = [{ path: '', component: SwipeComponent }];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class SwipeRoutingModule { }
