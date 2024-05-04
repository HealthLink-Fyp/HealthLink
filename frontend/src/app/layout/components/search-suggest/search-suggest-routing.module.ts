import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { SearchSuggestComponent } from './search-suggest.component';

const routes: Routes = [{ path: '', component: SearchSuggestComponent }];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class SearchSuggestRoutingModule { }
