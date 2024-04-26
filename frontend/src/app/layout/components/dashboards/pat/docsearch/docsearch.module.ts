import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { DocsearchRoutingModule } from './docsearch-routing.module';
import { DocsearchComponent } from './docsearch.component';


@NgModule({
  declarations: [
    DocsearchComponent
  ],
  imports: [
    CommonModule,
    DocsearchRoutingModule
  ]
})
export class DocsearchModule { }
