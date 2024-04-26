import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DocsearchComponent } from './docsearch.component';

const routes: Routes = [{ path: '', component: DocsearchComponent }];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class DocsearchRoutingModule { }
